import functools

product_list = [
    "P01-Tai Nghe Bluetooth-550000-4.5",
    "P02-Chuột Không Dây-250000-4.8",
    "P03-Bàn Phím Cơ-850000-4.5",
    "P04-Sạc Dự Phòng-300000",          
    "P05-Loa Bluetooth-250000VND-4.2"   
]

def hien_thi_tem_nhan(danh_sach):
    print("\n--- DANH SÁCH TEM NHÃN ---")
    for item in danh_sach:
        parts = item.split('-')
        
        try:
            ma = parts[0]
            ten = parts[1]
            gia_str = parts[2]
            rating_str = parts[3]
        except IndexError:
            ma_sp = parts[0] if len(parts) > 0 else "Unknown"
            print(f"Bỏ qua sản phẩm {ma_sp} do sai cấu trúc dữ liệu.")
            continue
            
        if not gia_str.isdigit():
            print(f"Bỏ qua sản phẩm {ma} do lỗi ép kiểu (giá tiền không hợp lệ).")
            continue
            
        thong_tin = {
            "ma": ma,
            "ten": ten,
            "gia": int(gia_str),
            "rating": rating_str
        }
        
        template = "Mã: {ma:<10} | Tên: {ten:<20} | Giá: {gia:,} VND | Rating: {rating}*"
        print(template.format_map(thong_tin))

def sap_xep_san_pham(danh_sach):
    def get_sort_key(item):
        parts = item.split('-')
        try:
            rating = float(parts[3])
            price = int(parts[2])
            return (-rating, price)
        except (IndexError, ValueError):
            return (0.0, float('inf')) 

    danh_sach.sort(key=get_sort_key)
    
    print("\n--- SẮP XẾP SẢN PHẨM ---")
    print("Đã sắp xếp thành công! Cập nhật danh sách:")
    for i, item in enumerate(danh_sach, 1):
        print(f"{i}. {item}")
        
    return danh_sach

def tinh_tong_gia_tri(danh_sach):
    prices = [int(p.split('-')[2]) for p in danh_sach if len(p.split('-')) >= 3 and p.split('-')[2].isdigit()]
    
    tong = functools.reduce(lambda acc, curr: acc + curr, prices, 0)
    
    print("\n--- TỔNG GIÁ TRỊ KHO ---")
    print(f"Tổng giá trị các mặt hàng hiện tại là: {tong:,} VND.")

def main():
    global product_list
    while True:
        print("\n============= E-COMMERCE ANALYTICS =============")
        print("1. Hiển thị tem nhãn sản phẩm (format_map & F-String)")
        print("2. Sắp xếp sản phẩm thông minh (sort key)")
        print("3. Tính tổng giá trị kho hàng (reduce)")
        print("4. Đóng hệ thống")
        print("================================================")
        
        choice = input("Chọn chức năng (1-4): ")
        
        match choice:
            case '1':
                hien_thi_tem_nhan(product_list)
            case '2':
                product_list = sap_xep_san_pham(product_list)
            case '3':
                tinh_tong_gia_tri(product_list)
            case '4':
                print("Đóng hệ thống. Tạm biệt!")
                break
            case _:
                print("Lựa chọn không hợp lệ, vui lòng thử lại.")

if __name__ == "__main__":
    main()