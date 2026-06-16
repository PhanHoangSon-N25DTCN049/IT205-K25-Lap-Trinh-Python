def display_records(attendance_book):
    """
    Chức năng 1: Xem bảng chấm công ngày.
    Sử dụng kỹ thuật định dạng chuỗi (String Formatting) cơ bản để căn lề.
    """
    print("\n--- BẢNG CHẤM CÔNG ---")
    
    if not attendance_book:
        print("Hệ thống chưa có dữ liệu chấm công.")
        return

    # In tiêu đề cột kèm theo căn lề cố định khoảng cách
    print(f"{'Mã NV':<6} | {'Tên Nhân Viên':<20} | {'Giờ Vào':<7} | {'Giờ Ra'}")
    print("-" * 50)

    # Duyệt danh sách và in dữ liệu
    for emp in attendance_book:
        clock_in = emp["times"][0]
        clock_out = emp["times"][1]
        
        # Nếu chưa chấm công ra (None) thì hiển thị trạng thái đang làm việc
        if clock_out is None:
            clock_out = "[Đang làm việc]"
            
        # Căn trái dữ liệu tương ứng với độ rộng tiêu đề để tạo thành hàng lối thẳng tắp
        print(f"{emp['id']:<6} | {emp['name']:<20} | {clock_in:<7} | {clock_out}")
        
    print("-" * 50)