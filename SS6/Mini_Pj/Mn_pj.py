laptop = 0
phone = 0
tablet = 0

while True:
    print("\n--- HỆ THỐNG QUẢN LÝ KHO ---")
    print("1. Xem báo cáo tồn kho")
    print("2. Nhập kho")
    print("3. Xuất kho")
    print("4. Cảnh báo hàng tồn kho thấp")
    print("5. Thoát chương trình")
    
    choice = input("Mời bạn chọn chức năng (1-5): ")
    
    match choice:
        case "1":
            print("\n--- BÁO CÁO TỒN KHO ---")
            print(f"Laptop: {laptop}")
            print(f"Điện thoại (Phone): {phone}")
            print(f"Máy tính bảng (Tablet): {tablet}")
            
            print("\n--- BIỂU ĐỒ TỒN KHO ---")
            print(f"Laptop ({laptop}): ", end="")
            for _ in range(laptop):
                print("*", end="")
            print()
            
            print(f"Phone ({phone}): ", end="")
            for _ in range(phone):
                print("*", end="")
            print()
            
            print(f"Tablet ({tablet}): ", end="")
            for _ in range(tablet):
                print("*", end="")
            print()

        case "2":
            print("\n--- NHẬP KHO ---")
            print("1. Laptop")
            print("2. Phone")
            print("3. Tablet")
            loai_hang = input("Chọn mặt hàng muốn nhập (1-3): ")
            
            match loai_hang:
                case "1" | "2" | "3":
                    while True:
                        so_luong = int(input("Nhập số lượng cần thêm: "))
                        if so_luong >= 0:
                            break
                        print("Số lượng không hợp lệ, vui lòng nhập lại!")
                    
                    match loai_hang:
                        case "1": laptop += so_luong
                        case "2": phone += so_luong
                        case "3": tablet += so_luong
                    print("Nhập kho thành công!")
                case _:
                    print("Lựa chọn mặt hàng không hợp lệ!")

        case "3":
            print("\n--- XUẤT KHO ---")
            print("1. Laptop")
            print("2. Phone")
            print("3. Tablet")
            loai_hang = input("Chọn mặt hàng muốn xuất (1-3): ")
            
            match loai_hang:
                case "1" | "2" | "3":
                    while True:
                        so_luong = int(input("Nhập số lượng cần xuất: "))
                        if so_luong >= 0:
                            break
                        print("Số lượng không hợp lệ, vui lòng nhập lại!")
                    
                    match loai_hang:
                        case "1":
                            if so_luong <= laptop:
                                laptop -= so_luong
                                print("Xuất kho thành công!")
                            else:
                                print("Không đủ hàng. Hủy giao dịch!")
                        case "2":
                            if so_luong <= phone:
                                phone -= so_luong
                                print("Xuất kho thành công!")
                            else:
                                print("Không đủ hàng. Hủy giao dịch!")
                        case "3":
                            if so_luong <= tablet:
                                tablet -= so_luong
                                print("Xuất kho thành công!")
                            else:
                                print("Không đủ hàng. Hủy giao dịch!")
                case _:
                    print("Lựa chọn mặt hàng không hợp lệ!")

        case "4":
            print("\n--- KIỂM TRA HÀNG TỒN KHO THẤP ---")
            co_canh_bao = False
            
            if laptop < 10:
                print(f"[CẢNH BÁO] Mặt hàng Laptop sắp hết (Chỉ còn {laptop} sản phẩm).")
                co_canh_bao = True
            if phone < 10:
                print(f"[CẢNH BÁO] Mặt hàng Điện thoại sắp hết (Chỉ còn {phone} sản phẩm).")
                co_canh_bao = True
            if tablet < 10:
                print(f"[CẢNH BÁO] Mặt hàng Máy tính bảng sắp hết (Chỉ còn {tablet} sản phẩm).")
                co_canh_bao = True
                
            if not co_canh_bao:
                print("Tất cả các mặt hàng đều ở mức an toàn (>= 10).")

        case "5":
            print("Đang thoát hệ thống... Tạm biệt!")
            break
            
        case _:
            print("Lựa chọn sai, vui lòng nhập lại từ 1 đến 5!");