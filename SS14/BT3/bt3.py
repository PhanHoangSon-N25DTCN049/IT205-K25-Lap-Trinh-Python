"""
Phân tích và thiết kế giải pháp cho hệ thống quản lý điểm thi Rikkei Academy.
Việc chia nhỏ chương trình thành các hàm chuyên biệt thay vì viết dồn vào một vòng lặp long mạch giúp mã nguồn trở nên sáng sủa,
dễ bảo trì, dễ kiểm thử độc lập và tái sử dụng được mã nguồn, tránh lặp lại logic như việc kiểm tra điểm hợp lệ hay tìm kiếm học viên.
Về thiết kế hệ thống, hàm phụ trợ validate_score nhận đầu vào là một chuỗi ký tự nhập từ bàn phím và trả về giá trị kiểu Boolean
là True nếu chuỗi đó có thể chuyển đổi thành số thực nằm trong đoạn từ 0 đến 10, ngược lại trả về False.
Hàm phụ trợ find_student_by_id nhận tham số là danh sách học viên và mã học viên cần tìm,
trả về chính dictionary của học viên đó nếu tìm thấy hoặc trả về None nếu không tồn tại.
Hàm phụ trợ get_rank nhận vào một số thực là điểm trung bình và trả về một chuỗi ký tự tương ứng với xếp loại học lực.
Đối với các hàm chức năng chính, hàm display_students nhận đầu vào là danh sách học viên và thực hiện in danh sách ra màn hình mà không trả về giá trị.
Hàm add_student nhận danh sách học viên, thực hiện các bước nhập liệu, chuẩn hóa chuỗi,
gọi các hàm phụ trợ để kiểm tra trùng mã hoặc điểm hợp lệ rồi thêm học viên mới vào danh sách gốc.
Hàm update_score nhận danh sách học viên, gọi hàm tìm kiếm để xác định học viên cần sửa, tiến hành cập nhật điểm mới sau khi đã xác thực.
Hàm evaluate_students nhận danh sách học viên, tính điểm trung bình và phối hợp với hàm xếp loại để hiển thị kết quả đánh giá cho toàn bộ danh sách.
Luồng chạy chính của chương trình sẽ nằm trong một vòng lặp vô hạn để hiển thị
menu và điều hướng luồng xử lý đến các hàm tương ứng dựa trên lựa chọn của người dùng.
"""

def validate_score(score_input):
    """Kiểm tra điểm số nhập vào có phải là số từ 0 đến 10 hay không"""
    try:
        score = float(score_input)
        if 0 <= score <= 10:
            return True
        return False
    except ValueError:
        return False

def find_student_by_id(student_list, student_id):
    """Tìm kiếm học viên theo mã học viên và trả về dictionary tương ứng"""
    for student in student_list:
        if student["student_id"] == student_id:
            return student
    return None

def get_rank(average_score):
    """Xếp loại học lực dựa trên điểm trung bình"""
    if average_score >= 8.0:
        return "Giỏi"
    elif average_score >= 6.5:
        return "Khá"
    elif average_score >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"

def display_students(student_list):
    """Hiển thị toàn bộ danh sách học viên hiện có"""
    if not student_list:
        print("Danh sách học viên hiện đang trống.")
        return
    for i, student in enumerate(student_list, 1):
        print(f"{i}. Mã: {student['student_id']} | Tên: {student['name']} | Toán: {student['math_score']} | Anh: {student['english_score']}")

def add_student(student_list):
    """Thêm học viên mới vào danh sách kèm theo các bước chuẩn hóa và kiểm tra dữ liệu"""
    while True:
        student_id = input("Nhập Mã Học Viên: ").strip().upper()
        if not student_id:
            print("Mã học viên không được để trống.")
            continue
        if find_student_by_id(student_list, student_id) is not None:
            print("Mã học viên đã tồn tại, vui lòng nhập mã khác!")
            continue
        break
    
    while True:
        name = input("Nhập Tên Học viên: ").strip()
        if not name:
            print("Tên học viên không được để trống.")
            continue
        name = name.title()
        break
        
    while True:
        math_input = input("Nhập Điểm Toán: ").strip()
        if validate_score(math_input):
            math_score = float(math_input)
            break
        print("Điểm không hợp lệ, phải là số từ 0 đến 10")
        
    while True:
        english_input = input("Nhập Điểm Anh: ").strip()
        if validate_score(english_input):
            english_score = float(english_input)
            break
        print("Điểm không hợp lệ, phải là số từ 0 đến 10")
        
    new_student = {
        "student_id": student_id,
        "name": name,
        "math_score": math_score,
        "english_score": english_score
    }
    student_list.append(new_student)
    print("Thêm học viên thành công!")

def update_score(student_list):
    """Cập nhật điểm thi của học viên dựa trên mã học viên được cung cấp"""
    student_id = input("Nhập mã học viên cần cập nhật: ").strip().upper()
    student = find_student_by_id(student_list, student_id)
    if student is None:
        print(f"Không tìm thấy học viên mang mã {student_id}!")
        return
        
    while True:
        math_input = input("Nhập Điểm Toán mới: ").strip()
        if validate_score(math_input):
            student["math_score"] = float(math_input)
            break
        print("Điểm không hợp lệ, phải là số từ 0 đến 10")
        
    while True:
        english_input = input("Nhập Điểm Anh mới: ").strip()
        if validate_score(english_input):
            student["english_score"] = float(english_input)
            break
        print("Điểm không hợp lệ, phải là số từ 0 đến 10")
    print("Cập nhật điểm thi thành công!")

def evaluate_students(student_list):
    """Tính điểm trung bình và xếp loại toàn bộ học viên trong danh sách"""
    if not student_list:
        print("Danh sách học viên hiện đang trống.")
        return
    for student in student_list:
        avg = (student["math_score"] + student["english_score"]) / 2
        rank = get_rank(avg)
        print(f"Mã: {student['student_id']} | Tên: {student['name']} | ĐTB: {avg:.2f} | Xếp loại: {rank}")

students = [
    {
        "student_id": "RA001",
        "name": "Nguyễn Văn A",
        "math_score": 8.5,
        "english_score": 7.0
    },
    {
        "student_id": "RA002",
        "name": "Trần Thị B",
        "math_score": 9.0,
        "english_score": 9.5
    }
]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ ĐIỂM THI RIKKEI ACADEMY =====")
    print("1. Hiển thị danh sách học viên")
    print("2. Thêm học viên mới")
    print("3. Cập nhật điểm thi theo mã học viên")
    print("4. Đánh giá học lực của toàn bộ học viên")
    print("5. Thoát chương trình")
    
    choice = input("Lựa chọn của bạn (1-5): ").strip()
    if choice == "1":
        display_students(students)
    elif choice == "2":
        add_student(students)
    elif choice == "3":
        update_score(students)
    elif choice == "4":
        evaluate_students(students)
    elif choice == "5":
        print("Cảm ơn bạn đã sử dụng hệ thống!")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")