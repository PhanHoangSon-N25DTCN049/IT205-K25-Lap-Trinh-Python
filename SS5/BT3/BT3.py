# (1) PHÂN TÍCH BÀI TOÁN & GIẢI PHÁP:
# - Input: Số lượng phòng, số hàng, số ghế mỗi hàng.
# - Output: Sơ đồ bằng dấu '*' hoặc thông báo lỗi.
# - Xử lý bẫy (Edge cases):
#   + Bẫy 1 (Phòng <= 0): Kết thúc ngay lập tức.
#   + Bẫy 2 (Hàng/Ghế <= 0): Dùng 'continue' để bỏ qua và sang phòng tiếp theo.
#   + Bẫy 3 (Hàng/Ghế > 10): Dùng 'break' để dừng toàn bộ quá trình nhập/in.

# (2) SOURCE CODE:
so_phong = int(input("Nhập số lượng phòng học cần kiểm tra: "))

# Xử lý Bẫy 1: Số lượng phòng không hợp lệ
if so_phong <= 0:
    print("Số lượng phòng học không hợp lệ")
else:
    for phong in range(1, so_phong + 1):
        print(f"\n--- Nhập thông tin phòng {phong} ---")
        so_hang = int(input("Nhập số hàng ghế: "))
        so_ghe = int(input("Nhập số ghế trên mỗi hàng: "))
        
        if so_hang <= 0 or so_ghe <= 0:
            print("Dữ liệu phòng học không hợp lệ. Bỏ qua phòng này")
            continue
            
        if so_hang > 10 or so_ghe > 10:
            print("Phòng quá lớn. Dừng nhập dữ liệu")
            break
            
        # In sơ đồ chỗ ngồi
        print(f"Sơ đồ phòng {phong}:")
        for hang in range(so_hang):
            # Nhân chuỗi '*' với số lượng ghế để in ra hàng
            print("*" * so_ghe)