"""
Hàm phụ trợ calculate_average được xây dựng để tính điểm trung bình cộng ba môn Toán, Lý, Hóa, giúp các chức năng khác không phải viết lại công thức này.
Đối với chức năng hiển thị (display_grades), chương trình kiểm tra danh sách rỗng để tránh lỗi, sau đó duyệt qua từng sinh viên,
tính điểm trung bình và phân loại học lực theo đúng các mốc quy định.
Ở chức năng cập nhật điểm (update_student_score),mã sinh viên nhập vào được chuẩn hóa bằng cách xóa khoảng trắng thừa và viết hoa toàn bộ để đảm bảo tìm kiếm chính xác.
Việc nhập điểm mới được đặt trong một vòng lặp vô hạn kết hợp với khối try-except để bắt lỗi ValueError khi nhập chữ,
đồng thời kiểm tra giá trị nằm trong khoảng 0-10. Chức năng thống kê (generate_report) đếm số lượng sinh viên đạt và trượt dựa trên mốc điểm trung bình 5.0,
từ đó tính toán tỷ lệ phần trăm. Chức năng tìm thủ khoa (find_valedictorian) thiết lập sinh viên đầu tiên làm mốc,
sau đó so sánh điểm trung bình với các sinh viên còn lại để tìm ra người có điểm cao nhất.
Toàn bộ luồng điều khiển được đặt trong hàm main() với một vòng lặp while True để duy trì menu tương tác cho đến khi nhận được lệnh thoát.
"""

student_records = [
    {
        "student_id": "SV001",
        "name": "Nguyễn Văn A",
        "math": 8.5,
        "physics": 7.0,
        "chemistry": 9.0
    },
    {
        "student_id": "SV002",
        "name": "Trần Thị B",
        "math": 4.0,
        "physics": 5.5,
        "chemistry": 5.0
    },
    {
        "student_id": "SV003",
        "name": "Lê Văn C",
        "math": 9.5,
        "physics": 9.0,
        "chemistry": 8.5
    }
]

def calculate_average(student):
    return (student["math"] + student["physics"] + student["chemistry"]) / 3

def display_grades(records):
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
        
    print("--- BẢNG ĐIỂM SINH VIÊN ---")
    for i, student in enumerate(records, 1):
        avg = calculate_average(student)
        rank = ""
        if avg >= 8.0:
            rank = "Giỏi"
        elif avg >= 6.5:
            rank = "Khá"
        elif avg >= 5.0:
            rank = "Trung bình"
        else:
            rank = "Yếu"
            
        print(f"{i}. [{student['student_id']}] {student['name']} | Toán: {student['math']} | Lý: {student['physics']} | Hóa: {student['chemistry']} | ĐTB: {avg:.2f} - {rank}")
    print("---------------------------")

def update_student_score(records):
    student_id = input("Nhập mã sinh viên cần cập nhật: ").strip().upper()
    
    target_student = None
    for student in records:
        if student["student_id"] == student_id:
            target_student = student
            break
            
    if target_student is None:
        print(f"Không tìm thấy sinh viên mang mã {student_id} trong hệ thống!")
        return
        
    print("Chọn môn học (1-Toán, 2-Lý, 3-Hóa):")
    choice = input("Lựa chọn: ").strip()
    
    subject_key = ""
    subject_name = ""
    if choice == "1":
        subject_key = "math"
        subject_name = "Toán"
    elif choice == "2":
        subject_key = "physics"
        subject_name = "Lý"
    elif choice == "3":
        subject_key = "chemistry"
        subject_name = "Hóa"
    else:
        print("Lựa chọn môn học không hợp lệ!")
        return
        
    while True:
        try:
            new_score = float(input("Nhập điểm mới: "))
            if 0 <= new_score <= 10:
                target_student[subject_key] = new_score
                print(f">> Đã cập nhật điểm {subject_name} của sinh viên '{target_student['name']}' thành {new_score}.")
                break
            else:
                print("Điểm số không hợp lệ. Vui lòng nhập từ 0 đến 10!")
        except ValueError:
            print("Điểm số không hợp lệ. Vui lòng nhập số!")

def generate_report(records):
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
        
    total_students = len(records)
    pass_count = 0
    
    for student in records:
        if calculate_average(student) >= 5.0:
            pass_count += 1
            
    fail_count = total_students - pass_count
    pass_rate = (pass_count / total_students) * 100
    fail_rate = (fail_count / total_students) * 100
    
    print("--- BÁO CÁO HỌC VỤ ---")
    print(f"Tổng số sinh viên: {total_students}")
    print(f"Số lượng qua môn (ĐTB >= 5.0): {pass_count} sinh viên (Chiếm {pass_rate:.2f}%)")
    print(f"Số lượng trượt (ĐTB < 5.0): {fail_count} sinh viên (Chiếm {fail_rate:.2f}%)")
    print("----------------------")

def find_valedictorian(records):
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return
        
    best_student = records[0]
    max_avg = calculate_average(records[0])
    
    for student in records[1:]:
        avg = calculate_average(student)
        if avg > max_avg:
            max_avg = avg
            best_student = student
            
    print("--- VINH DANH THỦ KHOA ---")
    print(f"Sinh viên: {best_student['name']} (Mã: {best_student['student_id']})")
    print(f"Điểm Trung Bình: {max_avg:.2f}")
    print("Chúc mừng sinh viên đã đạt thành tích xuất sắc nhất khóa!")
    print("--------------------------")

def main():
    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI UNIVERSITY =====")
        print("1. Xem bảng điểm và học lực")
        print("2. Cập nhật điểm thi sinh viên")
        print("3. Báo cáo thống kê (Đỗ/Trượt)")
        print("4. Tìm sinh viên Thủ khoa")
        print("5. Thoát chương trình")
        print("======================================================")
        
        choice = input("Chọn chức năng (1-5): ").strip()
        
        if choice == "1":
            display_grades(student_records)
        elif choice == "2":
            update_student_score(student_records)
        elif choice == "3":
            generate_report(student_records)
        elif choice == "4":
            find_valedictorian(student_records)
        elif choice == "5":
            print("Cảm ơn bạn đã sử dụng hệ thống!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn từ 1 đến 5.")

if __name__ == "__main__":
    main()