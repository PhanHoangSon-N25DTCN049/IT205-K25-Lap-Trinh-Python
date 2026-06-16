def normalize_student_names(records):
    """
    Chuẩn hóa chuỗi họ tên của toàn bộ sinh viên trong hệ thống.
    Bẫy 1: Kiểm tra danh sách rỗng.
    """
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    print("\n--- CHUẨN HÓA TÊN SINH VIÊN ---")
    for student in records:
        raw_name = student.get("name", "")
        # Tách từ bằng split() loại bỏ toàn bộ khoảng trắng thừa, viết hoa chữ cái đầu bằng title()
        clean_name = " ".join(raw_name.split()).title()
        student["name"] = clean_name
        print(f"{student['student_id']}: {clean_name}")
        
    print(">> Đã chuẩn hóa toàn bộ tên sinh viên.")