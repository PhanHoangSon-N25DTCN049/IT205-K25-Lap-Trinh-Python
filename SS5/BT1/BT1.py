# (1) PHÂN TÍCH LỖI:
# - Vì sao sai: Cách duyệt cũ đặt vòng lặp tháng ở ngoài và chi nhánh ở trong, 
#   khiến dữ liệu nhập vào bị xé lẻ theo tháng chứ không gom nhóm trọn vẹn theo từng chi nhánh.
# - Vòng lặp ngoài: Cần duyệt theo Chi nhánh.
# - Vòng lặp trong: Cần duyệt theo Tháng.

# (2) SỬA LỖI (SOURCE CODE ĐÃ ĐIỀU CHỈNH LẠI THỨ TỰ VÒNG LẶP):
so_chi_nhanh = 3
so_thang = 3
bao_cao = []

# Vòng lặp ngoài: Duyệt từng chi nhánh
for chi_nhanh in range(1, so_chi_nhanh + 1):
    
    # Vòng lặp trong: Duyệt từng tháng của chi nhánh hiện tại
    for thang in range(1, so_thang + 1):
        doanh_thu = int(input(f"Nhập doanh thu Chi nhánh {chi_nhanh}, tháng {thang}: "))
        bao_cao.append((chi_nhanh, thang, doanh_thu))

print("\n-------------- Kết quả --------------")

# Hiển thị kết quả (đã được gom chính xác theo từng chi nhánh)
for data in bao_cao:
    print(f"Chi nhánh {data[0]}, tháng {data[1]}: {data[2]} triệu đồng")