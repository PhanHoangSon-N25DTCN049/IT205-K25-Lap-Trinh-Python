"""
Để tối ưu hóa và tránh lặp lại đoạn mã tìm kiếm sinh viên trong từng chức năng, một hàm phụ trợ find_student được thiết kế để nhận vào danh sách hồ sơ và mã học viên
sau đó trả về vị trí (index) của học viên đó trong danh sách, hoặc trả về -1 nếu không tìm thấy.
Việc tách hàm này giúp mã nguồn gọn gàng hơn, dễ bảo trì và tái sử dụng khi cần xác thực mã ở các bước tiếp theo.
Đối với chức năng đổi thưởng (redeem_rewards), luồng xử lý bắt đầu bằng việc yêu cầu nhập mã học viên và dùng hàm strip().upper() để chuẩn hóa thành chữ in hoa,
loại bỏ khoảng trắng thừa. Sau khi gọi hàm find_student để xác nhận học viên tồn tại, hệ thống yêu cầu nhập số điểm cần tiêu.
Quá trình nhập này được đưa vào một vòng lặp vô hạn bảo vệ bởi khối try-except để bắt lỗi nếu dữ liệu nhập vào không phải là số nguyên.
Đồng thời, các điều kiện kiểm tra được thiết lập để đảm bảo điểm nhập vào phải là số dương và không được vượt quá số dư điểm hiện tại (current_points).
Nếu dữ liệu hợp lệ, hệ thống tiến hành trừ điểm ở current_points và cộng dồn vào spent_points. Đối với chức năng chấm bài (grade_assignment),
sau khi xác thực mã học viên thành công, hệ thống yêu cầu nhập điểm gốc đạt được với điều kiện phải là một số dương.
Điểm thực nhận được tính toán tự động bằng cách nhân điểm gốc với hệ số nhân (multiplier) đang áp dụng của học viên đó,
sau đó cộng trực tiếp vào quỹ điểm current_points. Các trường hợp ngoại lệ (Edge Cases) như nhập mã sai, tiêu quá số điểm,
hoàn số điểm lớn hơn số đã tiêu hay nhập hệ số ngoài khoảng 1.0 đến 3.0 đều được bẫy lỗi chặt chẽ thông qua các câu lệnh if-else,
đảm bảo chương trình không bị dừng đột ngột mà sẽ in ra cảnh báo và yêu cầu nhập lại.
Toàn bộ luồng điều khiển của chương trình được đặt trong hàm main() với một vòng lặp while True để duy trì tương tác hiển thị menu 6 chức năng.
"""

student_records = [
    {
        "student_id": "RA01",
        "name": "Nguyễn Văn Code",
        "current_points": 1500,
        "spent_points": 500,
        "refunded_points": 0,
        "multiplier": 1.0
    },
    {
        "student_id": "RA02",
        "name": "Trần Thị Bug",
        "current_points": 800,
        "spent_points": 1200,
        "refunded_points": 100,
        "multiplier": 1.5
    },
    {
        "student_id": "RA03",
        "name": "Lê Văn Fix",
        "current_points": 300,
        "spent_points": 0,
        "refunded_points": 0,
        "multiplier": 2.0
    }
]

def find_student(records, student_id):
    for index, student in enumerate(records):
        if student["student_id"] == student_id:
            return index
    return -1

def display_statements(records):
    print("--- SAO KÊ ĐIỂM SỐ ---")
    for i, student in enumerate(records, 1):
        status = ""
        if student["current_points"] < 500:
            status = "Cần tích lũy thêm"
        elif 500 <= student["current_points"] <= 1500:
            status = "Thành viên tiềm năng"
        else:
            status = "Thành viên ưu tú"
            
        print(f"{i}. Mã: {student['student_id']} | Tên: {student['name']} | Hiện có: {student['current_points']} | Đã tiêu: {student['spent_points']} | Hoàn trả: {student['refunded_points']} | Hệ số: x{student['multiplier']} | Trạng thái: {status}")
    print("----------------------")

def redeem_rewards(records):
    student_id = input("Nhập mã học viên đổi quà: ").strip().upper()
    index = find_student(records, student_id)
    
    if index == -1:
        print("Không tìm thấy hồ sơ học viên!")
        return
        
    while True:
        try:
            points_to_spend = int(input("Nhập số điểm cần tiêu: "))
            if points_to_spend <= 0:
                print("Số điểm tiêu phải là số nguyên dương lớn hơn 0!")
                continue
            if points_to_spend > records[index]["current_points"]:
                print("Số dư điểm không đủ để thực hiện giao dịch!")
                continue
            
            records[index]["current_points"] -= points_to_spend
            records[index]["spent_points"] += points_to_spend
            print(f">> Giao dịch thành công! '{records[index]['name']}' đã tiêu {points_to_spend} điểm. Số dư còn lại: {records[index]['current_points']} điểm.")
            break
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ!")

def appeal_score(records):
    student_id = input("Nhập mã học viên cần phúc khảo: ").strip().upper()
    index = find_student(records, student_id)
    
    if index == -1:
        print("Không tìm thấy hồ sơ học viên!")
        return
        
    while True:
        try:
            points_to_refund = int(input("Nhập số điểm hoàn lại: "))
            if points_to_refund <= 0:
                print("Số điểm hoàn phải là số nguyên dương lớn hơn 0!")
                continue
            if points_to_refund > records[index]["spent_points"]:
                print("Không thể hoàn số điểm lớn hơn tổng điểm đã tiêu!")
                continue
                
            records[index]["spent_points"] -= points_to_refund
            records[index]["current_points"] += points_to_refund
            records[index]["refunded_points"] += points_to_refund
            print(f">> Hoàn điểm thành công! '{records[index]['name']}' được cộng lại {points_to_refund} điểm.")
            break
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ!")

def activate_multiplier(records):
    student_id = input("Nhập mã học viên nhận hệ số: ").strip().upper()
    index = find_student(records, student_id)
    
    if index == -1:
        print("Không tìm thấy hồ sơ học viên!")
        return
        
    while True:
        try:
            new_multiplier = float(input("Nhập hệ số nhân mới (1.0 - 3.0): "))
            if 1.0 <= new_multiplier <= 3.0:
                records[index]["multiplier"] = new_multiplier
                print(f">> Đã kích hoạt hệ số x{new_multiplier} cho học viên '{records[index]['name']}'.")
                break
            else:
                print("Hệ số nhân không hợp lệ. Chỉ chấp nhận số từ 1.0 đến 3.0")
        except ValueError:
            print("Hệ số nhân không hợp lệ. Chỉ chấp nhận số từ 1.0 đến 3.0")

def grade_assignment(records):
    student_id = input("Nhập mã học viên vừa nộp bài: ").strip().upper()
    index = find_student(records, student_id)
    
    if index == -1:
        print("Không tìm thấy hồ sơ học viên!")
        return
        
    while True:
        try:
            base_score = float(input("Nhập số điểm gốc đạt được: "))
            if base_score <= 0:
                print("Điểm gốc phải là số dương lớn hơn 0!")
                continue
                
            multiplier = records[index]["multiplier"]
            actual_score = base_score * multiplier
            
            records[index]["current_points"] += int(actual_score) if actual_score.is_integer() else actual_score
            
            print(f">> Hệ số hiện tại của '{records[index]['name']}' là x{multiplier}. Điểm thực nhận: {actual_score:g}.")
            print(f">> Đã cộng {actual_score:g} điểm vào tài khoản!")
            break
        except ValueError:
            print("Vui lòng nhập một số hợp lệ!")

def main():
    while True:
        print("\n===== HỆ THỐNG NGÂN HÀNG ĐIỂM SỐ RIKKEI ACADEMY =====")
        print("1. Hiển thị sao kê điểm số")
        print("2. Đổi điểm lấy phần thưởng")
        print("3. Phúc khảo bài thi (Hoàn điểm)")
        print("4. Kích hoạt (Hệ số nhân điểm)")
        print("5. Chấm bài (thêm điểm)")
        print("6. Thoát chương trình")
        print("=====================================================")
        
        choice = input("Chọn chức năng (1-6): ").strip()
        
        if choice == "1":
            display_statements(student_records)
        elif choice == "2":
            redeem_rewards(student_records)
        elif choice == "3":
            appeal_score(student_records)
        elif choice == "4":
            activate_multiplier(student_records)
        elif choice == "5":
            grade_assignment(student_records)
        elif choice == "6":
            print("Chương trình kết thúc.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn từ 1 đến 6.")

if __name__ == "__main__":
    main()