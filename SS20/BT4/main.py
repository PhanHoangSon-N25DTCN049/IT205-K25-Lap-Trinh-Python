
# 1. Refactoring Plan (Clean Code & PEP 8):
#    - Đặt tên biến/hàm rõ nghĩa theo chuẩn snake_case thay cho các biến tối nghĩa 
#      như ds, p, l cũ (ví dụ: roster_list, player_record, calculate_actual_pay).
#    - Áp dụng Single Responsibility Principle (SRP): Mỗi hàm chỉ thực hiện đúng 
#      một nghiệp vụ duy nhất (Hàm hiển thị, hàm tính lương, hàm thêm mới...).
#    - Sử dụng Docstrings để giải thích rõ ràng chức năng, input và output của hàm.
# 
# 2. Logging Strategy:
#    - Tên file log: 'roster_app.log'
#    - Định dạng log: [%Y-%m-%d %H:%M:%S,%f] - [%(levelname)s] - %(message)s
#    - Các mức độ sử dụng: INFO (Thao tác thành công), WARNING (Lỗi người dùng nhập 
#      liệu sai, trùng ID), ERROR (Lỗi hệ thống thiếu trường dữ liệu quan trọng).
# 
# 3. Phân tích hàm update_player_status(roster_list):
#    - Input: roster_list (list chứa các dict tuyển thủ).
#    - Output: Thay đổi trực tiếp (mutable) thông tin lương hoặc trạng thái tuyển thủ trong list.
#    - Exceptions: 
#      + ValueError: Khi người dùng nhập lương mới là chữ ký tự lạ hoặc nhập số âm.
#      + Bẫy lỗi bằng vòng lặp while True để bắt nhập lại cho đến khi hợp lệ.
#    - Pseudocode:
#      Đọc player_id từ bàn phím -> Tìm kiếm player trong roster_list
#      Nếu không tìm thấy -> Ghi log WARNING, in thông báo, thoát hàm
#      Nếu tìm thấy -> Hiển thị thông tin hiện tại, cho chọn: 1-Cập nhật lương, 2-Cập nhật trạng thái
#      Nếu chọn 1 -> Vòng lặp nhập lương mới -> Kiểm tra số dương -> Cập nhật -> Ghi log INFO
#      Nếu chọn 2 -> Cho chọn 1-Active hoặc 2-Benched -> Cập nhật -> Ghi log INFO
# ==============================================================================

import logging

# Cấu hình logging ghi file hệ thống
logging.basicConfig(
    filename='roster_app.log',
    filemode='a',
    format='[%Y-%m-%d %H:%M:%S,%f] - [%(levelname)s] - %(message)s',
    level=logging.INFO
)

# Khởi tạo dữ liệu đội hình ban đầu
roster = [
    {
        "player_id": "P01",
        "name": "Faker",
        "role": "Mid Lane",
        "salary": 5000.0,
        "status": "Active"
    },
    {
        "player_id": "P02",
        "name": "Oner",
        "role": "Jungle",
        "salary": 3500.0,
        "status": "Active"
    },
    {
        "player_id": "P03",
        "name": "Ruler",
        "role": "ADC",
        "salary": 6000.0,
        "status": "Benched"
    }
]

def calculate_actual_pay(player_dict):
    """
    Hàm phụ trợ tính toán số lương thực nhận của tuyển thủ dựa trên trạng thái.
    Active nhận 100%, Benched nhận 50%.
    """
    if player_dict["status"] == "Active":
        return float(player_dict["salary"])
    elif player_dict["status"] == "Benched":
        return float(player_dict["salary"]) * 0.5
    return 0.0

def display_roster(roster_list):
    """Chức năng 1: Xem đội hình thi đấu hiện tại"""
    if not roster_list:
        print("\nĐội hình hiện đang trống.")
        logging.info("Coach viewed the team roster.")
        return

    print("\n--- ĐỘI HÌNH RIKKEI ESPORTS ---")
    print(f"{'ID':<8} | {'Tên tuyển thủ':<20} | {'Vị trí':<15} | {'Lương':<12} | Trạng thái")
    print("-" * 75)
    
    for player in roster_list:
        try:
            player_id = player["player_id"]
            role = player["role"]
            salary = f"{player['salary']:,}.0"
            status = player.get("status", "Unknown") # Bẫy dữ liệu thiếu status (Edge Case 1)
            
            # Xử lý hiển thị tag [DỰ BỊ] nếu status là Benched
            display_name = player["name"]
            if status == "Benched":
                display_name += " [DỰ BỊ]"
                
            print(f"{player_id:<8} | {display_name:<20} | {role:<15} | {salary:<12} | {status}")
        except KeyError as e:
            print(f"Lỗi: Tuyển thủ đang bị thiếu dữ liệu trường {e}!")
            
    logging.info("Coach viewed the team roster.")

def sign_player(roster_list):
    """Chức năng 2: Chiêu mộ tuyển thủ mới"""
    print("\n--- CHIÊU MỘ TUYỂN THỦ MỚI ---")
    player_id = input("Nhập mã tuyển thủ: ").strip().upper() # Chuẩn hóa mã rác
    
    if not player_id:
        print("Mã tuyển thủ không được để trống!")
        return

    # Kiểm tra trùng lặp ID tuyển thủ
    for player in roster_list:
        if player["player_id"] == player_id:
            print(f"\nLỗi: Mã tuyển thủ {player_id} đã tồn tại.")
            logging.warning(f"Failed to sign player - Duplicate player ID {player_id}")
            return

    name = input("Nhập tên tuyển thủ: ").strip()
    role = input("Nhập vị trí thi đấu: ").strip()
    
    # Bẫy lỗi nhập lương (Phải là số dương, ép nhập lại nếu gõ chữ hoặc số âm)
    while True:
        try:
            salary_input = input("Nhập mức lương hàng tháng: ").strip()
            salary = float(salary_input)
            if salary <= 0:
                print("\nLương phải là số dương. Vui lòng nhập lại.")
                continue
            break
        except ValueError:
            print("\nLương phải là số. Vui lòng nhập lại.")
            logging.warning("Failed to sign player - Invalid salary input")

    new_player = {
        "player_id": player_id,
        "name": name,
        "role": role,
        "salary": salary,
        "status": "Active"
    }
    roster_list.append(new_player)
    print(f"\nThành công: Đã chiêu mộ tuyển thủ {name}.")
    logging.info(f"Signed new player {name} with salary {salary}")

def update_player_status(roster_list):
    """Chức năng 3: Cập nhật lương & Trạng thái thi đấu"""
    print("\n--- CẬP NHẬT LƯƠNG & TRẠNG THÁI THI ĐẤU ---")
    player_id = input("Nhập mã tuyển thủ cần cập nhật: ").strip().upper()
    
    target_player = None
    for player in roster_list:
        if player["player_id"] == player_id:
            target_player = player
            break
            
    if not target_player:
        print(f"\nKhông tìm thấy tuyển thủ mang mã {player_id}.")
        logging.warning(f"Failed to update player - Player ID {player_id} not found")
        return

    print(f"\nTuyển thủ: {target_player['name']}")
    print(f"Vị trí: {target_player['role']}")
    print(f"Lương hiện tại: {target_player['salary']:,}.0")
    print(f"Trạng thái hiện tại: {target_player['status']}")
    
    print("\nBạn muốn cập nhật:")
    print("1. Cập nhật lương")
    print("2. Cập nhật trạng thái thi đấu")
    choice = input("Chọn chức năng cập nhật (1-2): ").strip()
    
    match choice:
        case "1":
            while True:
                try:
                    new_salary = float(input("Nhập mức lương mới: ").strip())
                    if new_salary <= 0:
                        print("Lương phải là số dương. Vui lòng nhập lại.")
                        continue
                    old_salary = target_player["salary"]
                    target_player["salary"] = new_salary
                    print(f"\nThành công: Đã cập nhật lương cho tuyển thủ {player_id}.")
                    logging.info(f"Updated player {player_id} salary from {old_salary} to {new_salary}")
                    break
                except ValueError:
                    print("Lương nhập vào không hợp lệ! Vui lòng gõ số dương.")
        case "2":
            print("\nChọn trạng thái mới:")
            print("1. Active")
            print("2. Benched")
            status_choice = input("Nhập lựa chọn trạng thái (1-2): ").strip()
            new_status = "Active" if status_choice == "1" else "Benched"
            
            target_player["status"] = new_status
            print(f"\nThành công: Đã cập nhật trạng thái cho tuyển thủ {player_id}.")
            logging.info(f"Updated player {player_id} status to {new_status}")
        case _:
            print("Lựa chọn không hợp lệ!")

def generate_payroll_report(roster_list):
    """Chức năng 4: Báo cáo quỹ lương hàng tháng"""
    print("\n--- BÁO CÁO QUỸ LƯƠNG HÀNG THÁNG ---")
    if not roster_list:
        print("Đội hình hiện đang trống. Tổng quỹ lương: 0.0")
        return

    print(f"{'ID':<8} | {'Tên tuyển thủ':<15} | {'Trạng thái':<10} | {'Lương gốc':<12} | Lương thực nhận")
    print("-" * 75)
    
    total_payroll = 0.0
    has_error = False
    
    for player in roster_list:
        try:
            actual_pay = calculate_actual_pay(player)
            total_payroll += actual_pay
            print(f"{player['player_id']:<8} | {player['name']:<15} | {player['status']:<10} | {player['salary']:<12,.1f} | {actual_pay:,.1f}")
        except KeyError as e:
            has_error = True
            logging.error(f"Missing key while generating payroll report: {e}")
            break
            
    print("-" * 75)
    if has_error:
        print("Lỗi: Một tuyển thủ đang bị thiếu dữ liệu.")
        print("Tổng quỹ lương hàng tháng: 0.0")
    else:
        print(f"Tổng quỹ lương hàng tháng: {total_payroll:,.1f}")
        logging.info(f"Generated monthly payroll report. Total: {total_payroll}")

def main():
    """Hàm chạy điều khiển luồng menu chính của hệ thống"""
    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ ĐỘI HÌNH RIKKEI ESPORTS =====")
        print("1. Xem đội hình thi đấu hiện tại")
        print("2. Chiêu mộ tuyển thủ mới")
        print("3. Cập nhật lương & Trạng thái thi đấu")
        print("4. Báo cáo quỹ lương hàng tháng")
        print("5. Thoát hệ thống")
        print("==================================================")
        
        choice = input("Chọn chức năng (1-5): ").strip()
        
        match choice:
            case "1":
                display_roster(roster)
            case "2":
                sign_player(roster)
            case "3":
                update_player_status(roster)
            case "4":
                generate_payroll_report(roster)
            case "5":
                print("\nHệ thống đang đóng. Hẹn gặp lại huấn luyện viên!")
                logging.info("System closed.")
                break
            case _:
                print("\nLựa chọn không hợp lệ! Vui lòng chọn từ 1 đến 5.")

if __name__ == "__main__":
    main()