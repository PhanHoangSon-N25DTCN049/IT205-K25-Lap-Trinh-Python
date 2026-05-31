
# 1. Phân tích Input / Output:
#    - Input:
#      + Dữ liệu lô hàng khai báo sẵn (Chuỗi thô): raw_batch
#      + Lựa chọn tính năng của người dùng từ giao diện CLI (Menu từ 1 đến 4).
#      + Giá trị tìm kiếm khi dùng tính năng tra cứu (Chuỗi nhập vào từ bàn phím).
#    - Output:
#      + Giao diện tương tác trực quan qua CLI.
#      + Dữ liệu hiển thị chi tiết theo từng chức năng (Dạng chuỗi gốc, dạng bảng báo cáo, hoặc kết quả tra cứu).

# 2. Đề xuất giải pháp và các hàm xử lý:
#    - Sử dụng cấu trúc vòng lặp vô hạn `while True` để duy trì menu hệ thống cho đến khi chọn Thoát.
#    - Dùng phương thức `.strip()` để xử lý khoảng trắng thô ở mọi đầu vào (Menu, Tra cứu, Thành phần mã).
#    - Dùng `.split(";")` để tách các sản phẩm trong lô hàng và `.split("-")` để bóc tách 4 thành phần của mã sản phẩm.
#    - Sử dụng phương thức `.upper()` để chuẩn hóa toàn bộ các ký tự mã về dạng chữ in hoa hệ thống.
#    - Dùng phương thức ép kiểu kiểm tra kiểm định `.isdigit()` trên chuỗi Serial để phát hiện và xử lý bẫy lỗi dữ liệu.
#    - Dùng cơ chế định dạng chuỗi f-string kết hợp căn lề `<` hoặc `^` để thiết lập bảng báo cáo kiểm kê cân đối.

# 3. Thiết kế thuật toán (Pseudocode):
#    Khai báo raw_batch = " LAP-VN-23-001 ; mou-us-24-012 ; KEY-vn-23-abc ; lap-JP-22-045 ; MOn-vn-24-099 "
#    Vòng lặp vô hạn:
#        Hiển thị danh sách Menu chức năng (1-4)
#        Nhập lua_chon từ người dùng
#        Xóa khoảng trắng lua_chon
#        Nếu lua_chon == "1":
#            In ra chuỗi dữ liệu gốc raw_batch
#        Nếu lua_chon == "2":
#            Tách raw_batch bằng dấu ";"
#            In tiêu đề bảng (MÃ SP | XUẤT XỨ | NĂM SX | SERIAL | TRẠNG THÁI)
#            Khởi tạo các biến đếm hợp lệ và tổng số sản phẩm
#            Vòng lặp duyệt qua từng mã sản phẩm sau khi tách:
#                Làm sạch và chuyển in hoa toàn bộ mã
#                Tách mã thành 4 thành phần bằng dấu "-"
#                Nếu phần số Serial (3 ký tự cuối) chỉ chứa số:
#                    Trạng thái = "Pass", tăng biến đếm hợp lệ lên 1
#                Ngược lại:
#                    Trạng thái = "Lỗi Serial - Reject"
#                Chuyển đổi Năm sản xuất (Thêm "20" vào trước)
#                In dòng thông tin sản phẩm căn lề chuẩn dạng bảng
#            In tổng kết: Số sản phẩm hợp lệ / Tổng số sản phẩm
#        Nếu lua_chon == "3":
#            Nhập đuôi serial cần tìm, làm sạch bằng .strip()
#            Đặt biến đánh dấu tìm thấy = False
#            Vòng lặp duyệt qua từng mã trong lô hàng:
#                Tách mã thành các thành phần sạch
#                Lấy 2 ký tự cuối của Serial so sánh với chuỗi vừa nhập
#                Nếu trùng khớp:
#                    In thông tin sản phẩm và đổi trạng thái tìm thấy thành True
#            Nếu tìm thấy == False: In thông báo không tìm thấy sản phẩm phù hợp
#        Nếu lua_chon == "4":
#            In thông báo đóng ca và kết thúc vòng lặp (break)
#        Ngược lại:
#            In thông báo lỗi nhập sai menu và quay lại vòng lặp


# Nguồn dữ liệu lô hàng cố định được khai báo sẵn trong hệ thống
raw_batch = " LAP-VN-23-001 ; mou-us-24-012 ; KEY-vn-23-abc ; lap-JP-22-045 ; MOn-vn-24-099 "

while True:
    # Hiển thị cấu trúc menu CLI quản lý kho hàng
    print("\n===== HỆ THỐNG GIẢI MÃ DỮ LIỆU KHO HÀNG =====")
    print("1. Hiển thị chuỗi mã vạch gốc")
    print("2. Giải mã, làm sạch và in báo cáo kiểm kê")
    print("3. Tra cứu nhanh theo đuôi Serial")
    print("4. Thoát chương trình")
    
    user_choice = input("Nhập lựa chọn của bạn (1-4): ").strip()
    
    # CHỨC NĂNG 1: Hiển thị dữ liệu gốc trực tiếp từ máy quét
    if user_choice == "1":
        print("\n--- CHUỖI MÃ VẠCH GỐC ---")
        print(raw_batch)
        
    # CHỨC NĂNG 2: Giải mã dữ liệu và xử lý nghiệp vụ, bẫy dữ liệu lỗi
    elif user_choice == "2":
        print("\n--- BÁO CÁO KIỂM KÊ LÔ HÀNG ---")
        # Định dạng tiêu đề bảng sử dụng toán tử f-string căn lề thẳng hàng gọn gàng
        print(f"{'MÃ SP':<15} | {'XUẤT XỨ':<10} | {'NĂM SX':<8} | {'SERIAL':<8} | {'TRẠNG THÁI'}")
        print("-" * 60)
        
        # Tách nhỏ lô hàng thành danh sách các chuỗi sản phẩm riêng biệt
        products = raw_batch.split(";")
        total_products = 0
        valid_products = 0
        
        for prod in products:
            clean_prod = prod.strip()
            if not clean_prod:  # Bỏ qua nếu xuất hiện phần tử rỗng do dấu phân tách thừa
                continue
                
            total_products += 1
            # Chuyển đổi mã sản phẩm sang chữ in hoa chuẩn hóa hệ thống
            upper_prod = clean_prod.upper()
            
            # Tách nhỏ mã sản phẩm thành 4 thuộc tính cấu trúc
            parts = upper_prod.split("-")
            
            product_type = parts[0]
            country = parts[1]
            short_year = parts[2]
            serial = parts[3]
            
            # Chuẩn hóa dữ liệu năm sản xuất sang định dạng 4 chữ số
            full_year = f"20{short_year}"
            
            # Bẫy 1 — Kiểm tra tính hợp lệ và định dạng của số Serial
            if serial.isdigit():
                status = "Pass"
                valid_products += 1
            else:
                status = "Lỗi Serial - Reject"
                
            # Đẩy thông tin sản phẩm hoàn chỉnh lên dòng hiển thị của bảng báo cáo
            print(f"{upper_prod:<15} | {country:<10} | {full_year:<8} | {serial:<8} | {status}")
            
        print("-" * 60)
        print(f"Tổng kết: Đã giải mã thành công {valid_products} sản phẩm hợp lệ / Tổng số {total_products} sản phẩm.")
        
    # CHỨC NĂNG 3: Tìm kiếm tra cứu thông tin sản phẩm nhanh bằng 2 số cuối Serial
    elif user_choice == "3":
        # Bẫy 2 — Nhập dư khoảng trắng khi tiến hành tra cứu dữ liệu
        search_query = input("Nhập 2 số cuối của Serial cần tìm: ").strip()
        print(f"\n--- KẾT QUẢ TRA CỨU ĐUÔI SERIAL '{search_query}' ---")
        
        products = raw_batch.split(";")
        found_any = False
        
        for prod in products:
            clean_prod = prod.strip()
            if not clean_prod:
                continue
                
            upper_prod = clean_prod.upper()
            parts = upper_prod.split("-")
            serial = parts[3]
            
            # So sánh chuỗi tìm kiếm với 2 ký tự cuối (đuôi) của mã định danh Serial sản phẩm
            if serial[-2:] == search_query:
                # Trích xuất thông tin xuất xứ quốc gia và năm sản xuất chuẩn hóa
                country = parts[1]
                full_year = f"20{parts[2]}"
                print(f"Tìm thấy sản phẩm: {upper_prod} [Xuất xứ: {country}, Năm SX: {full_year}, Serial: {serial}]")
                found_any = True
                
        if not found_any:
            print("Không tìm thấy sản phẩm phù hợp")
            
    # CHỨC NĂNG 4: Kết thúc tiến trình ca kiểm kho hệ thống
    elif user_choice == "4":
        print("\nĐóng ca kiểm kho. Chào tạm biệt!")
        break
        
    # BẪY 3: Xử lý lỗi nhập sai định dạng hoặc phạm vi lựa chọn trên menu hệ thống
    else:
        print("\nChức năng không tồn tại, vui lòng nhập số từ 1-4!")