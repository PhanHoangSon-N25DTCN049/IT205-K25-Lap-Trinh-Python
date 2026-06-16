import math
import os
import datetime

# ==============================================================================
# PHẦN 1: ĐÁP ÁN CÂU HỎI LÝ THUYẾT (ARCHITECTURE REVIEW)
# ==============================================================================
"""
1. Tại sao lạm dụng 'from math import *' là một "Anti-pattern"?
   - Gây ô nhiễm không gian tên (Namespace Pollution): Nạp quá nhiều hàm không dùng tới vào bộ nhớ.
   - Dễ xảy ra xung đột tên hàm: Nếu bạn tự viết một hàm tên là 'sqrt', nó sẽ đè lên hàm 'sqrt' của thư viện, 
     hoặc ngược lại, gây lỗi hệ thống rất khó kiểm soát.
   * Giải pháp an toàn: Chỉ import chính xác những hàm cần dùng, ví dụ: from math import sin, cos, sqrt

2. Tệp cấu hình biến thư mục thành Package:
   - Đó là tệp '__init__.py'.
   - Vai trò: Đánh dấu thư mục đó là một Package hợp lệ trong Python để có thể import từ nơi khác. 

3. Sơ đồ cấu trúc cây thư mục (Folder Tree) nếu tách file:
   Rikkei_Logistics/
   ├── core/
   │   ├── __init__.py
   │   ├── geo_calculator.py
   │   └── time_estimator.py
   ├── utils/
   │   ├── __init__.py
   │   └── file_helper.py
   └── main.py
"""

# ==============================================================================
# PHẦN 2: TRIỂN KHAI CÁC HÀM CHỨC NĂNG (MÔ PHỎNG CÁC MODULE)
# ==============================================================================

# --- Mô phỏng utils/file_helper.py ---
def create_log_dir(dir_name):
    """
    Kiểm tra an toàn nếu thư mục chưa tồn tại mới tiến hành tạo,
    tránh lỗi FileExistsError khi chạy lại chương trình.
    """
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
        return True
    return False


# --- Mô phỏng core/geo_calculator.py ---
def calculate_distance(lat1, lon1, lat2, lon2):
    """
    Tính khoảng cách giữa 2 điểm trên mặt cầu theo công thức Haversine (đơn vị: km).
    """
    # Bán kính Trái Đất (km)
    R = 6371.0

    # Chuyển đổi tọa độ từ độ (degree) sang radians
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    # Áp dụng công thức Haversine chính xác
    a = (math.sin(delta_phi / 2) ** 2 +
         math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c


# --- Mô phỏng core/time_estimator.py ---
def predict_eta(departure_str, distance_km, speed=60):
    """
    Tính toán thời gian dự kiến đến nơi (ETA) dựa trên thời gian khởi hành,
    khoảng cách và vận tốc xe chạy.
    """
    # Ép kiểu chuỗi thời gian thành đối tượng datetime
    dep_time = datetime.datetime.strptime(departure_str, "%Y-%m-%d %H:%M:%S")
    
    # Tính số giờ cần thiết để di chuyển
    hours_needed = distance_km / speed
    
    # Tính toán ETA bằng cách cộng thêm khoảng thời gian di chuyển vào thời điểm xuất phát
    eta = dep_time + datetime.timedelta(hours=hours_needed)
    return eta


# ==============================================================================
# PHẦN 3: ĐIỀU PHỐI VÀ XỬ LÝ DỮ LIỆU CHÍNH (MAIN FUNCTION)
# ==============================================================================

# Dữ liệu đầu vào giả lập từ tổng đài
shipments = [
    {
        "id": "TRK-001", 
        "from_lat": 21.0285, "from_lon": 105.8542, 
        "to_lat": 10.8231, "to_lon": 106.6297, 
        "depart": "2026-06-10 08:00:00", 
        "deadline": "2026-06-11 12:00:00"
    },
    {
        "id": "TRK-002", 
        "from_lat": 21.0285, "from_lon": 105.8542, 
        "to_lat": 16.0544, "to_lon": 108.2022, 
        "depart": "2026-06-10 09:30:00", 
        "deadline": "2026-06-10 15:00:00"
    },
]

def main():
    print("====== HỆ THỐNG ĐIỀU PHỐI RIKKEI LOGISTICS =======")
    
    # Gọi hàm tạo thư mục log an toàn (không bị crash khi chạy lại lần 2)
    create_log_dir("logs")
    print("[INFO] Khởi tạo hệ thống lưu trữ log hành trình... Thành công.")
    print("-" * 75)

    # Duyệt qua danh sách các chuyến xe để tính toán và kiểm tra tiến độ
    for s in shipments:
        # 1. Tính toán khoảng cách chính xác bằng Haversine
        distance = calculate_distance(s["from_lat"], s["from_lon"], s["to_lat"], s["to_lon"])
        
        # 2. Dự báo thời gian cập bến (ETA) với vận tốc mặc định 60 km/h
        eta = predict_eta(s["depart"], distance, speed=60)
        
        # 3. Chuyển chuỗi hạn định (deadline) về dạng datetime để so sánh chính xác
        deadline_time = datetime.datetime.strptime(s["deadline"], "%Y-%m-%d %H:%M:%S")
        
        # 4. Kiểm tra trạng thái tiến độ dựa trên so sánh logic datetime
        if eta <= deadline_time:
            status = "🟢 AN TOÀN (Kịp tiến độ trước deadline)"
        else:
            # Lấy giờ:phút:giây của deadline để hiển thị cảnh báo chuẩn format yêu cầu
            deadline_str_time = deadline_time.strftime("%H:%M:%S")
            status = f"🔴 CẢNH BÁO (Trễ hạn! Deadline yêu cầu lúc {deadline_str_time})"
            
        # 5. Xuất kết quả ra console theo đúng khuôn mẫu kết quả kỳ vọng
        print(f"[CHUYẾN XE {s['id']}]")
        print(f" + Khoảng cách vận chuyển: {distance:.2f} km")
        print(f" + Thời gian khởi hành: {s['depart']}")
        print(f" + Dự kiến cập bến (ETA): {eta.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f" + Trạng thái: {status}\n")

    print("=" * 56)

# Điểm kích hoạt chương trình chạy
if __name__ == "__main__":
    main()