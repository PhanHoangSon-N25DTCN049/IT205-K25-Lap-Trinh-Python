from core.logistics import display_flights_logistics
from core.manager import accept_new_flight
from utils.time_helper import calculate_flight_eta
from utils.file_helper import initialize_log_directory

# Dữ liệu khởi tạo ban đầu của Rikkei Aviation
flights = [
    {"flight_id": "RA001", "passengers": 154, "depart_time": "2026-06-15 08:00:00", "duration_min": 120},
    {"flight_id": "RA002", "passengers": 85,  "depart_time": "2026-06-15 13:30:00", "duration_min": 45}
]

def main():
    while True:
        print("\n===== HỆ THỐNG ĐIỀU HÀNH BAY RIKKEI AVIATION =====")
        print("1. Hiển thị lịch trình và Thống kê hậu cần")
        print("2. Tiếp nhận chuyến bay mới")
        print("3. Tính thời gian hạ cánh dự kiến (ETA)")
        print("4. Khởi tạo thư mục lưu trữ log hệ thống")
        print("5. Thoát chương trình")
        print("==================================================")
        
        # Bẫy lỗi nhập ký tự lạ tại Menu chính (Edge Case 4)
        try:
            choice = int(input("Nhập lựa chọn của bạn: "))
        except ValueError:
            print("🔴 LỖI: Vui lòng nhập số nguyên từ 1 đến 5!")
            continue

        # Điều hướng Menu sử dụng cấu trúc case theo yêu cầu
        match choice:
            case 1:
                display_flights_logistics(flights)
            case 2:
                accept_new_flight(flights)
            case 3:
                calculate_flight_eta(flights)
            case 4:
                initialize_log_directory()
            case 5:
                print("Cảm ơn kỹ sư đã sử dụng hệ thống!")
                break
            case _:
                print("🔴 LỖI: Lựa chọn không hợp lệ! Vui lòng nhập lại (1-5).")

if __name__ == "__main__":
    main()