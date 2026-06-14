import logging


# 1. Quản lý ngoại lệ (Exception Handling): 
#    - Dùng try...except ValueError tại chức năng 3 để ép trọng tài nhập lại điểm 
#      nếu cố tình nhập chữ ("hai", "một") hoặc nhập điểm âm (< 0).
#    - Dùng try...except KeyError khi trích xuất dữ liệu phòng trường hợp API thiếu key.
# 2. Logic bẫy ẩn (Edge Case 0-0): Trận đấu chỉ được coi là "Completed" tự động 
#    nếu ít nhất một đội có điểm > 0. Nếu cả hai đội bằng 0, hệ thống buộc trọng 
#    tài phải xác nhận (y/n) có thực sự kết thúc trận đấu hay không.
# 3. Đặt tên biến/hàm tuân thủ chuẩn PEP 8 (snake_case, rõ nghĩa, self-documenting).

# Cấu hình thư viện logging ghi file theo định dạng chuẩn
logging.basicConfig(
    filename='tournament_app.log',
    filemode='a',
    format='[%Y-%m-%d %H:%M:%S,%f] - [%(levelname)s] - %(message)s',
    level=logging.INFO
)

# Dữ liệu khởi tạo hệ thống giải đấu
matches = [
    {
        "match_id": "M01",
        "team_a": "T1",
        "team_b": "GenG",
        "score_a": 2,
        "score_b": 1,
        "status": "Completed"
    },
    {
        "match_id": "M02",
        "team_a": "JDG",
        "team_b": "BLG",
        "score_a": 0,
        "score_b": 0,
        "status": "Pending"
    }
]

def determine_winner(match):
    """
    Hàm phụ trợ xác định đội chiến thắng dựa trên kết quả trận đấu.
    @param match: dict chứa thông tin trận đấu
    @return: Tên đội thắng, 'Draw' hoặc 'Not Started'
    """
    try:
        if match.get("status") == "Pending":
            return "Not Started"
        
        score_a = match["score_a"]
        score_b = match["score_b"]
        
        if score_a > score_b:
            return match["team_a"]
        elif score_b > score_a:
            return match["team_b"]
        else:
            return "Draw"
    except KeyError as e:
        logging.error(f"Missing key in match data: {e}")
        return "Data Error"

def display_matches(match_list):
    """Chức năng 1: Hiển thị lịch thi đấu & Kết quả"""
    if not match_list:
        print("\nHiện chưa có trận đấu nào trong hệ thống.")
        logging.info("User viewed the match list.")
        return

    print("\n--- LỊCH THI ĐẤU & KẾT QUẢ ---")
    print(f"{'Mã trận':<10} | {'Đội A':<15} | {'Đội B':<15} | {'Tỷ số':<7} | Trạng thái")
    print("-" * 70)
    
    for m in match_list:
        try:
            score_str = f"{m['score_a']}-{m['score_b']}"
            print(f"{m['match_id']:<10} | {m['team_a']:<15} | {m['team_b']:<15} | {score_str:<7} | {m['status']}")
        except KeyError:
            print(f"{m.get('match_id', 'N/A'):<10} | Lỗi trích xuất dữ liệu dòng này!")
            
    logging.info("User viewed the match list.")

def add_match(match_list):
    """Chức năng 2: Thêm trận đấu mới"""
    print("\n--- THÊM TRẬN ĐẤU MỚI ---")
    match_id = input("Nhập mã trận đấu: ").strip()
    
    if not match_id:
        print("\nMã trận đấu không được để trống.")
        logging.warning("User tried to add a match with empty match ID.")
        return
        
    # Kiểm tra trùng lặp ID
    for m in match_list:
        if m["match_id"] == match_id:
            print(f"\nLỗi: Mã trận đấu {match_id} đã tồn tại.")
            logging.warning(f"Match ID {match_id} already exists.")
            return

    team_a = input("Nhập tên Đội A: ").strip()
    team_b = input("Nhập tên Đội B: ").strip()
    
    if not team_a or not team_b:
        print("\nTên đội không được để trống.")
        logging.warning("User tried to add a match with empty team name.")
        return

    new_match = {
        "match_id": match_id,
        "team_a": team_a,
        "team_b": team_b,
        "score_a": 0,
        "score_b": 0,
        "status": "Pending"
    }
    match_list.append(new_match)
    print(f"\nThành công: Đã thêm trận đấu {match_id}.")
    logging.info(f"Match {match_id} added successfully")

def update_score(match_list):
    """Chức năng 3: Cập nhật tỷ số trận đấu"""
    print("\n--- CẬP NHẬT TỶ SỐ TRẬN ĐẤU ---")
    match_id = input("Nhập mã trận đấu cần cập nhật: ").strip()
    
    target_match = None
    for m in match_list:
        if m["match_id"] == match_id:
            target_match = m
            break
            
    if not target_match:
        print(f"\nKhông tìm thấy trận đấu mang mã {match_id}.")
        logging.warning(f"User tried to update non-existing match {match_id}")
        return

    print(f"\nTrận đấu: {target_match['team_a']} vs {target_match['team_b']} ({target_match['status']})")
    
    # Bẫy lỗi nhập điểm đội A
    while True:
        try:
            input_a = input("Nhập điểm Đội A: ").strip()
            score_a = int(input_a)
            if score_a < 0:
                print("\nĐiểm số phải lớn hơn hoặc bằng 0.")
                logging.error(f"Negative score input detected: {score_a}")
                continue
            break
        except ValueError as e:
            print("\nĐiểm số phải là số nguyên. Vui lòng nhập lại.")
            logging.error(f"Invalid score input. Error: {e}")

    # Bẫy lỗi nhập điểm đội B
    while True:
        try:
            input_b = input("Nhập điểm Đội B: ").strip()
            score_b = int(input_b)
            if score_b < 0:
                print("\nĐiểm số phải lớn hơn hoặc bằng 0.")
                logging.error(f"Negative score input detected: {score_b}")
                continue
            break
        except ValueError as e:
            print("\nĐiểm số phải là số nguyên. Vui lòng nhập lại.")
            logging.error(f"Invalid score input. Error: {e}")

    # Xử lý Edge Case lỗi logic ẩn tỷ số 0-0
    status = "Completed"
    if score_a == 0 and score_b == 0:
        confirm = input("Tỷ số đang là 0-0. Trọng tài có xác nhận trận đã hoàn thành không? (y/n): ").strip().lower()
        if confirm != 'y':
            status = "Pending"

    # Tiến hành cập nhật dữ liệu dữ dội
    target_match["score_a"] = score_a
    target_match["score_b"] = score_b
    target_match["status"] = status
    
    print(f"\nThành công: Đã cập nhật tỷ số trận đấu {match_id}.")
    logging.info(f"Match {match_id} score updated successfully")

def generate_report(match_list):
    """Chức năng 4: Báo cáo thống kê"""
    print("\n--- BÁO CÁO THỐNG KÊ GIẢI ĐẤU ---")
    completed_count = 0
    
    for m in match_list:
        if m.get("status") == "Completed":
            winner = determine_winner(m)
            print(f"{m['match_id']}: {m['team_a']} {m['score_a']}-{m['score_b']} {m['team_b']} | Kết quả: {winner}")
            completed_count += 1
            
    if completed_count == 0:
        print("Chưa có trận đấu nào hoàn thành.")
        
    print(f"\nTổng số trận đã hoàn thành: {completed_count}")
    logging.info("User generated tournament report.")

def main():
    """Hàm chạy chương trình chính điều khiển menu luồng xử lý"""
    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ GIẢI ĐẤU RIKKEI ESPORTS =====")
        print("1. Hiển thị lịch thi đấu & Kết quả")
        print("2. Thêm trận đấu mới")
        print("3. Cập nhật tỷ số trận đấu")
        print("4. Báo cáo thống kê")
        print("5. Thoát chương trình")
        print("==================================================")
        
        choice = input("Chọn chức năng (1-5): ").strip()
        
        # Mặc định sử dụng cấu trúc case để phân tách tính năng
        match choice:
            case "1":
                display_matches(matches)
            case "2":
                add_match(matches)
            case "3":
                update_score(matches)
            case "4":
                generate_report(matches)
            case "5":
                print("\nHệ thống đang đóng. Tạm biệt!")
                logging.info("System shutdown and exit.")
                break
            case _:
                print("\nLựa chọn không hợp lệ! Vui lòng chọn từ 1 đến 5.")
                logging.warning("Invalid menu choice selected")

if __name__ == "__main__":
    main()