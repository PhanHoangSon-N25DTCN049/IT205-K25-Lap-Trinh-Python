"""
trong đoạn code của hệ thống điều kiện nhịp tim > 100 được cho kiểm tra đầu tiên nếu nó đúng 
các điều khiện sau sẽ không được kiểm tra trong trường hợp nhịp tim lớn hơn 120 chương trình cũng chỉ xét đến > 100 mà k xét đến lớn hơn 120
 
Trong cấu trúc rẽ nhánh đa nhánh (if-elif-else), luồng thực thi hoạt động theo quy tắc "thỏa mãn là dừng":
Máy tính kiểm tra các điều kiện từ trên xuống dưới.
Gặp điều kiện nào ĐÚNG đầu tiên, nó sẽ chạy khối lệnh tương ứng rồi thoát ngay lập tức khỏi toàn bộ cấu
trúc if-elif-else, bỏ qua tất cả các nhánh elif hoặc else phía dưới.
"""

heart_rate = int(input("Enter patient's heart rate (bpm): "));

# Kiểm tra mức độ nguy kịch nhất trước
if heart_rate > 120:
    print("Priority: RED - Critical condition! Immediate action required.")
elif heart_rate > 100:
    print("Priority: YELLOW - Abnormal. Monitor closely.")
elif heart_rate < 60:
    print("Priority: BLUE - Bradycardia. Require ultrasound.")
else:
    print("Priority: GREEN - Stable. Please wait in the lobby.") 
 



