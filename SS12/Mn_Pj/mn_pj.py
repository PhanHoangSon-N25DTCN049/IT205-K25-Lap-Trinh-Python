def menu ():
    print("============================================")
    print("     QUẢN LÝ BÃI XE - SMART PARKING ")
    print("============================================")
    print("  1. Check-in (Đăng ký xe vào)");
    print("  2. Báo cáo tồn kho (Hiển thị danh sách)");
    print("  3. Tìm kiếm theo xe (Theo biển số)");
    print("  4. Check-out (Xử lý xe ra và tính phí)");
    print("  5. Thoát chương trình");
    print("============================================");
    


auto_id = 1;
park = [];
while True:
    menu();
    choice = input("Nhập lựa chọn của bạn (1-5): ").strip();
    
    match choice:
        case "5":
            print("Thoát chương trình");
            break;
        case "1":
            while True:
                plate = input("Nhập biển số xe: ").strip();
                if not plate:
                    print("Biển số xe không được bỏ trống!");
                    continue;
                
                check_plate = False;
                for car in park:
                    if plate == car["plate"]:
                        check_plate = True;
                        break;
                if check_plate:
                    print(f"Biển số {plate} đã tồn tại trong bãi! vui lòng kiểm tra lại.");
                else:
                    break;
            
            while True:
                type = input("Nhập loại xe (1: Xe máy / 2: Ô tô): ");
                if type == "1" or type == "2": 
                    break;
                else: 
                    print("Lỗi lựa chọn vui lòng nhập lại!");
            
            while True:
                entry_time = input("Nhập thời gian vào bãi(0 -> 24): ").strip();
                if entry_time == "":
                    print("thời gian vào không được bỏ trống!");
                elif not entry_time.isdigit(): 
                    print("dữ liệu nhập vào phải là số");
                elif int(entry_time) > 24 or int(entry_time) < 0:
                    print("khoảng thời gian không hợp lệ");
                else: break;
            
            new_car = {
                "id": auto_id,
                "plate": plate,
                "type": type,
                "entry_time": entry_time
            };
            auto_id += 1;
            park.append(new_car);
            print("Đăng ký xe vào thành công");
        case "2":
            if not park:
                print("[Thông báo: Bãi xe hiện đang trống!]");
                continue;
            header = f"{"ID":<5} | {"Biển số xe":<15} | {"Loại xe":<7} | {"Giờ vào":<8}";
            print(header);
            print("-"*len(header));
            for car in park:
                print(f"{car["id"]:<5} | {car["plate"]:<15} | {car["type"]:<7} | {car["entry_time"]:<8}");
            print("-"*len(header));
        case "3":
            while True:
                search_plate = input("Nhập biển số xe cần tìm: ").strip();
                if search_plate: break;
                print("Biển số xe không được bỏ trống!");
                
            check_plate = True;
            for car in park:
                if search_plate == car["plate"]:
                    print(f"Thông tin chi tiết: {car}");
                    check_plate = False;
                    break;
            if check_plate:
                print(f"[Lỗi: Không tìm thấy biển số {search_plate} trong hệ thống!]");
        case "4":
            while True:
                plate_out = input("Nhập biển số xe cần ra: ").strip();
                if plate_out: break;
                print("Biển số xe không được bỏ trống!");
                
            temp_idx = -1;
            for idx, car in enumerate(park):
                if plate_out == car["plate"]:
                    temp_idx = idx;
                    break;
            
            if temp_idx == -1:
                print(f"[Lỗi]: Không tìm thấy biển số {plate_out} trong hệ thống");
                continue;
            
            while True:
                time_left = input("Nhập thời gian rời bãi(0 -> 24): ").strip();
                if time_left == "":
                    print("thời gian vào không được bỏ trống!");
                elif not time_left.isdigit(): 
                    print("dữ liệu nhập vào phải là số");
                elif int(time_left) > 24 or int(time_left) < 0:
                    print("khoảng thời gian không hợp lệ");
                elif int(time_left) < int(park[temp_idx]["entry_time"]):
                    print("Thời gian ra phải sau hoặc bằng thời gian vào!");
                else: break;
            print(f"Tổng phí phải trả: {(int(time_left) - int(park[temp_idx]['entry_time']))*5000} VND");
            print(f"[Thành công]: Đã xóa xe ID {park[temp_idx]['id']} thành công");
            del park[temp_idx];
        case _:
            print("Lỗi lựa chọn! vui lòng nhập lại");
                    
        