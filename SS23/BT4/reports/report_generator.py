from datetime import datetime
from colorama import Fore, Style, init
from utils.score_utils import calculate_average, classify_student

# Khởi tạo colorama tự động reset màu sau mỗi dòng lệnh in
init(autoreset=True)

def display_student_scores(records):
    """
    Hiển thị danh sách sinh viên kèm điểm trung bình và xếp loại học lực.
    Bẫy 1: Kiểm tra danh sách rỗng.
    """
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    print("\n--- DANH SÁCH ĐIỂM SINH VIÊN ---")
    for idx, student in enumerate(records, 1):
        scores = student.get("scores", [])
        avg = calculate_average(scores)
        classification = classify_student(avg)
        
        # Định dạng hiển thị canh lề tên sinh viên để báo cáo đều đẹp
        print(f"{idx}. [{student['student_id']}] {student['name']:<15} | Điểm: {scores} | ĐTB: {avg:.2f} - {classification}")
    print("-" * 33)

def export_learning_report(records):
    """
    Tính toán thống kê và kết xuất dữ liệu ra file learning_report.txt.
    Sử dụng thư viện bên thứ ba colorama để đổi màu thông báo.
    """
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    total_students = len(records)
    passed_students = 0
    failed_students = 0

    for student in records:
        avg = calculate_average(student.get("scores", []))
        if avg >= 5.0:
            passed_students += 1
        else:
            failed_students += 1

    print("\n--- XUẤT BÁO CÁO HỌC TẬP ---")
    print(f"Tổng số sinh viên: {total_students}")
    print(f"Số sinh viên đạt yêu cầu: {passed_students}")
    print(f"Số sinh viên cần cải thiện: {failed_students}")

    # Ghi nội dung báo cáo ra file text kèm thời gian hệ thống
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("learning_report.txt", "w", encoding="utf-8") as f:
        f.write("=========================================\n")
        f.write("         BÁO CÁO KẾT QUẢ HỌC TẬP         \n")
        f.write(f"Thời gian khởi tạo: {current_time}\n")
        f.write("=========================================\n")
        f.write(f"Tổng số sinh viên cấu hình: {total_students}\n")
        f.write(f"Số sinh viên đạt yêu cầu (ĐTB >= 5.0): {passed_students}\n")
        f.write(f"Số sinh viên cần cải thiện (ĐTB < 5.0): {failed_students}\n")
        f.write("-----------------------------------------\n")

    # Hiển thị thông báo thành công có màu xanh lá (GREEN)
    print(Fore.GREEN + Style.BRIGHT + ">> Đã xuất báo cáo ra file learning_report.txt")