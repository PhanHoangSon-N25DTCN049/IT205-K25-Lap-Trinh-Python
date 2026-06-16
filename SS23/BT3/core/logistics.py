import math

def display_flights_logistics(flight_list):
    """
    Chức năng 1: Duyệt qua danh sách, tính số thùng nước khoáng dự phòng 
    bằng hàm math.ceil (cứ 10 hành khách cần 1 thùng).
    """
    print("\n----- DANH SÁCH CHUYẾN BAY & HẬU CẦN -----")
    if not flight_list:
        print("Hiện chưa có chuyến bay nào trong hệ thống.")
        return
        
    for idx, flight in enumerate(flight_list, 1):
        passengers = flight["passengers"]
        # Cứ 10 hành khách thì cần 1 thùng nước dự phòng, làm tròn lên
        water_blocks = math.ceil(passengers / 10)
        
        print(f"{idx}. Mã: {flight['flight_id']} | "
              f"Khởi hành: {flight['depart_time']} | "
              f"Số khách: {passengers:<3} | "
              f"Dự phòng: {water_blocks} thùng nước.")