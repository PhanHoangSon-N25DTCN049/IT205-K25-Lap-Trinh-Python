from datetime import datetime

def evaluate_flex_time(attendance_book):
    """
    Chức năng 4: Đánh giá vi phạm (Module chuẩn).
    Áp dụng chính xác luật Flex-time để kiểm tra tiến độ làm việc.
    """
    print("\n--- ĐÁNH GIÁ VI PHẠM (LUẬT FLEX-TIME) ---")
    if not attendance_book:
        print("Hệ thống chưa có dữ liệu để đánh giá.")
        return

    # Khung giờ mốc quy định để so sánh
    max_late_time = datetime.strptime("10:00", "%H:%M")

    for emp in attendance_book:
        time_in_str = emp["times"][0]
        time_out_str = emp["times"][1]

        # Chỉ xử lý khi nhân viên đã có đủ cả Giờ Vào và Giờ Ra
        if time_in_str and time_out_str:
            # Chuyển đổi chuỗi "HH:MM" thành đối tượng datetime để tính toán
            t_in = datetime.strptime(time_in_str, "%H:%M")
            t_out = datetime.strptime(time_out_str, "%H:%M")

            # 1. Kiểm tra nếu Giờ vào > 10:00 (Muộn quá 90 phút)
            if t_in > max_late_time:
                print(f"❌ {emp['id']} - Vi phạm: Đến muộn quá 90 phút (Vào lúc {time_in_str}).")
            else:
                # 2. Nếu giờ vào hợp lệ, tính hiệu số thời gian làm việc (Giờ Ra - Giờ Vào)
                work_duration = t_out - t_in
                total_seconds = work_duration.total_seconds()
                hours_worked = total_seconds / 3600

                # Kiểm tra xem có đủ 9 tiếng làm việc bù giờ hay không
                if hours_worked < 9.0:
                    print(f"❌ {emp['id']} - Vi phạm: Về sớm, chưa hoàn thành đủ 9 tiếng bù giờ (Mới làm {hours_worked:.2f} tiếng).")
                else:
                    print(f"✅ {emp['id']} - Hợp lệ: Hoàn thành ca làm việc.")