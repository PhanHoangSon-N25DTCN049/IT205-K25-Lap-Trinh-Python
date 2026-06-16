def clock_in(attendance_book):
    """
    Chức năng 2: Chấm công Vào (Clock-in).
    Tiếp nhận nhân viên mới, bẫy lỗi trùng Mã NV.
    """
    print("\n--- CHẤM CÔNG VÀO (CLOCK-IN) ---")
    emp_id = input("Nhập mã nhân viên: ").strip().upper()
    
    # Bẫy lỗi: Kiểm tra trùng mã nhân viên trong danh sách
    for emp in attendance_book:
        if emp["id"] == emp_id:
            print(f"🔴 LỖI: Mã nhân viên '{emp_id}' đã tồn tại trên hệ thống!")
            return

    name = input("Nhập tên nhân viên: ").strip()
    time_in = input("Nhập giờ vào (HH:MM): ").strip()

    # Tạo mới dictionary với tuple times là (time_in, None)
    new_record = {
        "id": emp_id,
        "name": name,
        "times": (time_in, None)
    }
    
    attendance_book.append(new_record)
    print(f"🟢 Thành công: Đã ghi nhận {emp_id} chấm công vào lúc {time_in}!")


def clock_out(attendance_book):
    """
    Chức năng 3: Chấm công Ra (Clock-out).
    Tìm nhân viên, trích xuất giờ vào cũ và ghi đè Tuple mới hoàn toàn.
    """
    print("\n--- CHẤM CÔNG RA (CLOCK-OUT) ---")
    emp_id = input("Nhập mã nhân viên cần chấm công ra: ").strip().upper()
    
    target_emp = None
    for emp in attendance_book:
        if emp["id"] == emp_id:
            target_emp = emp
            break
            
    if not target_emp:
        print(f"🔴 LỖI: Không tìm thấy nhân viên có mã {emp_id}!")
        return

    time_out = input("Nhập giờ ra (HH:MM): ").strip()

    # XỬ LÝ TUPLE CỐT LÕI: Trích xuất Giờ Vào cũ từ tuple vị trí số 0
    time_in_old = target_emp["times"][0]
    
    # Tạo một Tuple hoàn toàn mới kết hợp (Giờ Vào cũ, Giờ Ra mới) và ghi đè vào key 'times'
    target_emp["times"] = (time_in_old, time_out)
    
    print(f"🟢 Thành công: Đã ghi nhận {emp_id} chấm công ra lúc {time_out}!")