from datetime import datetime

def check_duplicate_id(flight_id, flight_list):
    """
    Helper Function: Kiểm tra trùng mã chuyến bay (chuẩn hóa strip và upper).
    """
    clean_id = flight_id.strip().upper()
    for flight in flight_list:
        if flight["flight_id"] == clean_id:
            return True
    return False

def accept_new_flight(flight_list):
    """
    Chức năng 2: Tiếp nhận và chuẩn hóa dữ liệu chuyến bay mới, bẫy lỗi đầu vào.
    """
    print("\n----- TIẾP NHẬN CHUYẾN BAY MỚI -----")
    
    # 1. Bẫy lỗi trùng mã chuyến bay (Edge Case 1)
    raw_id = input("Nhập mã chuyến bay: ")
    if check_duplicate_id(raw_id, flight_list):
        print(f"🔴 LỖI: Mã chuyến bay '{raw_id.strip().upper()}' đã tồn tại trên hệ thống!")
        return

    # 2. Nhập số lượng hành khách
    try:
        passengers = int(input("Nhập số lượng hành khách: "))
        if passengers < 0:
            print("🔴 LỖI: Số lượng hành khách không được âm!")
            return
    except ValueError:
        print("🔴 LỖI: Số lượng hành khách phải là một số nguyên!")
        return

    # 3. Bẫy lỗi định dạng ngày tháng khởi hành (Edge Case 2)
    depart_time_str = input("Nhập thời gian cất cánh (YYYY-MM-DD HH:MM:SS): ")
    try:
        # Thử ép kiểu để kiểm tra tính hợp lệ của chuỗi thời gian
        datetime.strptime(depart_time_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        print("🔴 LỖI: Sai định dạng thời gian! Vui lòng nhập đúng chuẩn YYYY-MM-DD HH:MM:SS")
        return

    # 4. Nhập số phút bay
    try:
        duration_min = int(input("Nhập số phút bay: "))
        if duration_min <= 0:
            print("🔴 LỖI: Số phút bay phải lớn hơn 0!")
            return
    except ValueError:
        print("🔴 LỖI: Số phút bay phải là một số nguyên!")
        return

    # Thêm chuyến bay hợp lệ vào database tạm thời
    new_flight = {
        "flight_id": raw_id.strip().upper(),
        "passengers": passengers,
        "depart_time": depart_time_str,
        "duration_min": duration_min
    }
    flight_list.append(new_flight)
    print(f">> Thêm chuyến bay {new_flight['flight_id']} thành công!")