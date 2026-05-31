# 1. Phân tích Input / Output:
#    - Input:
#      + Số lượng phiếu đăng ký (Kiểu số nguyên n).
#      + Chuỗi đăng ký thô (Kiểu chuỗi str): "Họ tên | Tên khóa học | Mã học viên | Email"
#    - Output:
#      + Thông báo lỗi nếu dính các bẫy dữ liệu (Edge Cases).
#      + Chuỗi kết quả đã chuẩn hóa theo đúng định dạng nghiệp vụ yêu cầu.

# 2. Đề xuất giải pháp và các hàm xử lý:
#    - Dùng vòng lặp kiểm tra điều kiện nhập số lượng phiếu hợp lệ (> 0).
#    - Sử dụng vòng lặp for kết hợp range(n) để duyệt qua từng phiếu đăng ký.
#    - Dùng .strip() và .split("|") để bóc tách cấu trúc dữ liệu.
#    - Sử dụng các string methods phù hợp để chuẩn hóa:
#      + Họ tên: .title() (Viết hoa chữ cái đầu mỗi từ).
#      + Tên khóa học: .title() (Chuẩn hóa chữ hoa/thường).
#      + Mã học viên: .upper() (Viết in hoa toàn bộ).
#      + Email: .lower() (Chuyển về chữ thường hệ thống).
#      + Mã xác nhận: Kết hợp Mã học viên và Tên khóa học (thay khoảng trắng bằng '-').

# 3. Thiết kế thuật toán (Pseudocode):
#    Nhập số lượng phiếu n
#    Nếu n <= 0:
#        In ra "Số lượng phiếu đăng ký không hợp lệ" và dừng chương trình
#    Vòng lặp i chạy từ 1 đến n:
#        Nhập chuỗi raw_string
#        Tách chuỗi thành danh sách các phần tử bằng dấu '|'
#        Nếu số phần tử != 4:
#            In ra lỗi và bỏ qua phiếu này (continue)
#        Làm sạch khoảng trắng từng phần tử
#        Nếu mã học viên có độ dài < 5:
#            In ra lỗi và bỏ qua phiếu này (continue)
#        Nếu email không chứa ký tự '@':
#            In ra lỗi và bỏ qua phiếu này (continue)
#        Chuẩn hóa định dạng các trường thông tin
#        Tạo mã xác nhận: Mã học viên + "_" + Tên khóa học (In hoa và thay khoảng trắng bằng dấu '-')
#        In ra kết quả phiếu đã chuẩn hóa



def main():
    # Bước 1: Nhập và kiểm tra số lượng phiếu đăng ký (Bẫy 1)
    try:
        num_forms = int(input("Nhập số lượng phiếu đăng ký cần xử lý: "))
    except ValueError:
        print("Số lượng phiếu đăng ký không hợp lệ")
        return

    if num_forms <= 0:
        print("Số lượng phiếu đăng ký không hợp lệ")
        return

    # Duyệt qua từng phiếu đăng ký theo số lượng đã nhập
    for i in range(1, num_forms + 1):
        print(f"\n--- Nhập dữ liệu cho phiếu thứ {i} ---")
        raw_input = input("Chuỗi đăng ký: ")

        # Bước 2: Tách chuỗi dữ liệu thô bằng dấu '|'
        parts = [part.strip() for part in raw_input.split("|") if raw_input.strip()]

        # Bẫy 2: Kiểm tra chuỗi nhập có đủ 4 phần dữ liệu không
        if len(parts) != 4:
            print("Dữ liệu đăng ký không hợp lệ. Bỏ qua phiếu này")
            continue

        # Trích xuất dữ liệu tạm thời để kiểm tra điều kiện
        raw_name, raw_course, raw_student_id, raw_email = parts

        # Bẫy 4: Kiểm tra độ dài mã học viên (Phải từ 5 ký tự trở lên)
        if len(raw_student_id) < 5:
            print("Mã học viên không hợp lệ. Bỏ qua phiếu này")
            continue

        # Bẫy 3: Kiểm tra tính hợp lệ của email (Phải chứa ký tự '@')
        if "@" not in raw_email:
            print("Email không hợp lệ. Bỏ qua phiếu này")
            continue

        # Bước 3: Chuẩn hóa dữ liệu theo đúng nghiệp vụ yêu cầu
        student_name = raw_name.title()
        course_name = raw_course.title()
        student_id = raw_student_id.upper()
        email = raw_email.lower()

        # Tạo mã xác nhận tự động: [Mã học viên]_[Tên khóa học viết hoa liền nhau bằng dấu -]
        # Ví dụ: Python Basic -> PYTHON-BASIC
        course_slug = course_name.upper().replace(" ", "-")
        confirmation_code = f"{student_id}_{course_slug}"

        # Bước 4: Hiển thị kết quả đầu ra đã được chuẩn hóa thành công
        print("===== PHIẾU ĐĂNG KÝ ĐÃ CHUẨN HÓA =====")
        print(f"Học viên: {student_name}")
        print(f"Khóa học: {course_name}")
        print(f"Mã học viên: {student_id}")
        print(f"Email: {email}")
        print(f"Mã xác nhận: {confirmation_code}")

if __name__ == "__main__":
    main()