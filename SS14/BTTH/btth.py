"""
Dữ liệu cốt lõi là một danh sách chứa các dictionary, trong đó mỗi dictionary lưu thông tin của một học sinh
Điểm đặc biệt của bài toán này là việc sử dụng tuple để lưu trữ điểm số môn Toán và môn Anh. Do tuple là kiểu dữ liệu bất biến (immutable),
chương trình không thể thay đổi trực tiếp từng phần tử bên trong (ví dụ như gán giá trị mới cho info[0]).
Thay vào đó, khi cần cập nhật điểm trong hàm update_scores, bắt buộc phải tạo ra một tuple hoàn toàn mới chứa điểm Toán và điểm Anh vừa nhập,
sau đó ghi đè toàn bộ tuple mới này vào key "info" của dictionary tương ứng.
Chức năng thêm mới (add_student) cần kiểm tra mã học sinh để tránh trùng lặp trước khi đóng gói thông tin vào dictionary và nối thêm vào danh sách. 
Chức năng xóa (delete_student) sẽ duyệt qua danh sách để tìm vị trí của học sinh và loại bỏ phần tử đó. 
Chức năng hiển thị (display_grades) truy xuất điểm từ tuple, tính toán điểm trung bình và dùng f-string để căn lề in ra dạng bảng. 
Toàn bộ luồng chức năng được gọi thông qua menu điều hướng đặt trong hàm main().
"""

def display_grades(book):
    print("--- BẢNG ĐIỂM HỌC SINH ---")
    print(f"{'Mã SV':<5} | {'Tên Học Sinh':<19} | {'Điểm Toán':<9} | {'Điểm Anh':<8} | {'ĐTB'}")
    print("-" * 71)
    for student in book:
        math_score = student["info"][0]
        english_score = student["info"][1]
        average = (math_score + english_score) / 2
        print(f"{student['id']:<5} | {student['name']:<19} | {math_score:<9.1f} | {english_score:<8.1f} | {average:.2f}")
    print("-" * 71)

def add_student(book):
    student_id = input("Nhập mã học sinh mới: ").strip().upper()
    
    for student in book:
        if student["id"] == student_id:
            print(f"Lỗi: Mã học sinh {student_id} đã tồn tại! Vui lòng nhập mã khác.")
            return
            
    name = input("Nhập tên học sinh: ").strip()
    math_score = float(input("Nhập điểm Toán: "))
    english_score = float(input("Nhập điểm Anh: "))
    
    new_student = {
        "id": student_id,
        "name": name,
        "info": (math_score, english_score)
    }
    book.append(new_student)
    print(f"Thành công: Đã thêm học sinh {student_id} vào hệ thống!")

def update_scores(book):
    student_id = input("Nhập mã học sinh cần cập nhật: ").strip().upper()
    
    for student in book:
        if student["id"] == student_id:
            new_math = float(input("Nhập điểm Toán mới: "))
            new_english = float(input("Nhập điểm Anh mới: "))
            student["info"] = (new_math, new_english)
            print(f"Thành công: Đã cập nhật điểm cho học sinh {student_id}!")
            return
            
    print("Lỗi: Không tìm thấy hồ sơ học sinh!")

def delete_student(book):
    student_id = input("Nhập mã học sinh cần xóa: ").strip().upper()
    
    for index, student in enumerate(book):
        if student["id"] == student_id:
            del book[index]
            print(f"Thành công: Đã xóa hồ sơ học sinh {student_id} khỏi hệ thống!")
            return
            
    print("Lỗi: Không tìm thấy hồ sơ học sinh!")

def main():
    grade_book = [
        {"id": "SV01", "name": "Nguyễn Văn A", "info": (8.5, 7.0)},
        {"id": "SV02", "name": "Trần Thị B", "info": (6.0, 9.0)}
    ]
    
    while True:
        print("\n=== HỆ THỐNG QUẢN LÝ ĐIỂM SỐ ===")
        print("1. Xem bảng điểm học sinh")
        print("2. Thêm hồ sơ học sinh mới")
        print("3. Cập nhật điểm số")
        print("4. Xóa hồ sơ học sinh")
        print("5. Thoát chương trình")
        print("================================")
        
        choice = input("Chọn chức năng (1-5): ").strip()
        
        if choice == "1":
            display_grades(grade_book)
        elif choice == "2":
            add_student(grade_book)
        elif choice == "3":
            update_scores(grade_book)
        elif choice == "4":
            delete_student(grade_book)
        elif choice == "5":
            print("Cảm ơn bạn đã sử dụng hệ thống. Hẹn gặp lại!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn từ 1 đến 5.")

if __name__ == "__main__":
    main()