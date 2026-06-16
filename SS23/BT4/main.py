from data.students import student_records
from utils.string_utils import normalize_student_names
from utils.random_utils import generate_assignment_code
import reports.report_generator as rg  # Sử dụng alias import nâng cao

def main():
    while True:
        print("\n===== HỆ THỐNG TIỆN ÍCH HỌC TẬP RIKKEI ACADEMY =====")
        print("1. Xem danh sách sinh viên và điểm trung bình")
        print("2. Chuẩn hóa tên sinh viên")
        print("3. Sinh mã bài tập ngẫu nhiên")
        print("4. Xuất báo cáo học tập")
        print("5. Thoát chương trình")
        print("====================================================")
        
        # Bẫy 4: Kiểm tra dữ liệu đầu vào khi người dùng chọn sai định dạng hoặc nhập chữ
        try:
            choice = int(input("Chọn chức năng (1-5): "))
        except ValueError:
            print("Chức năng không hợp lệ. Vui lòng chọn từ 1 đến 5.")
            continue

        # Áp dụng cấu trúc rẽ nhánh điều hướng mặc định bằng case
        match choice:
            case 1:
                rg.display_student_scores(student_records)
            case 2:
                normalize_student_names(student_records)
            case 3:
                generate_assignment_code()
            case 4:
                rg.export_learning_report(student_records)
            case 5:
                print("Cảm ơn bạn đã sử dụng hệ thống!")
                break
            case _:
                print("Chức năng không hợp lệ. Vui lòng chọn từ 1 đến 5.")

if __name__ == "__main__":
    main()