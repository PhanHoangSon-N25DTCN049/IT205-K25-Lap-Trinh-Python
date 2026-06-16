# Cấu trúc dữ liệu khởi tạo mẫu (Mock Data) theo đề bài yêu cầu
attendance_book = [
    {"id": "NV01", "name": "Nguyễn Văn A", "times": ("08:30", "17:30")},
    {"id": "NV02", "name": "Trần Thị B", "times": ("09:30", None)}, 
    {"id": "NV03", "name": "Lê Văn C", "times": ("10:15", "19:15")}
]

# Advanced Import: Áp dụng cú pháp đổi tên (alias) theo đúng Quy định nộp bài
from hrm_package.ui_display import display_records as show_table
from hrm_package.attendance_logic import clock_in as record_in, clock_out as record_out
from hrm_package.time_calc import evaluate_flex_time as evaluate_shifts

def main():
    while True:
        print("\n=== HỆ THỐNG CHẤM CÔNG RIKKEI (FLEX-TIME) ===")
        print("1. Xem bảng chấm công ngày")
        print("2. Chấm công Vào (Clock-in)")
        print("3. Chấm công Ra (Clock-out)")
        print("4. Đánh giá vi phạm")
        print("5. Thoát chương trình")
        print("=============================================")
        
        # Bẫy lỗi: Kiểm tra định dạng khi người dùng nhập chữ hoặc ký tự lạ vào menu
        try:
            choice = int(input("Chọn chức năng (1-5): "))
        except ValueError:
            print("🔴 LỖI: Vui lòng nhập một số nguyên hợp lệ từ 1 đến 5!")
            continue

        # Điều hướng xử lý menu bằng cấu trúc rẽ nhánh case mặc định
        match choice:
            case 1:
                show_table(attendance_book)
            case 2:
                record_in(attendance_book)
            case 3:
                record_out(attendance_book)
            case 4:
                evaluate_shifts(attendance_book)
            case 5:
                print("Hệ thống đóng. Cảm ơn bạn đã sử dụng dịch vụ của Rikkei HRM!")
                break
            case _:
                print("🔴 LỖI: Chức năng không nằm trong danh mục. Vui lòng chọn lại (1-5).")

if __name__ == "__main__":
    main()