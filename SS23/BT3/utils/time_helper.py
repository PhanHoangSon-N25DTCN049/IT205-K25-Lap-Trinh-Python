from datetime import datetime, timedelta

def calculate_flight_eta(flight_list):
    """
    Chức năng 3: Tìm chuyến bay theo ID và tính toán thời gian hạ cánh dự kiến (ETA).
    """
    print("\n----- TÍNH TOÁN THỜI GIAN HẠ CÁNH (ETA) -----")
    search_id = input("Nhập mã chuyến bay cần tính: ").strip().upper()
    
    target_flight = None
    for flight in flight_list:
        if flight["flight_id"] == search_id:
            target_flight = flight
            break
            
    if not target_flight:
        print(f"🔴 Không tìm thấy chuyến bay nào có mã {search_id}.")
        return
        
    # Xử lý tính toán thời gian bằng thư viện datetime
    depart_time = datetime.strptime(target_flight["depart_time"], "%Y-%m-%d %H:%M:%S")
    duration = timedelta(minutes=target_flight["duration_min"])
    eta_time = depart_time + duration
    
    print(f"-> Chuyến bay {search_id} cất cánh lúc: {target_flight['depart_time']}")
    print(f"-> Thời gian hạ cánh dự kiến (ETA): {eta_time.strftime('%Y-%m-%d %H:%M:%S')}")