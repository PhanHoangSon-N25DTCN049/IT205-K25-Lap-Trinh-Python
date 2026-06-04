auto_id = 101;
staff_manager = [];
while True:
    print("=======================================");
    print("   Quản lý nhân sự - STAFF MANAGER");
    print("=======================================");
    print("1. Thêm nhân viên mới");
    print("2. Danh sách nhân viên");
    print("3. Xóa nhân viên khỏi hệ thống");
    print("4. Thoát chương trình");
    print("=======================================");
    choice = input("Nhập lựa chọn (1->4): ");
    match choice:
        case "4":
            print("Thoát chương trình");
            break;
        case "1":
            while True:
                name = input("Tên nhân viên: ").strip();
                if name:
                    break;
                print("Tên nhân viên không được để trống");
            
            while True:
                salary = input("Nhập lương nhân viên: ").strip();
                if not salary:
                    print("Lương nhân viên không được để trống");
                elif not salary.lstrip("-").isdigit():
                    print("vui lòng nhập số");
                elif float(salary) < 0:
                    print("Lương phải >= 0");
                else: break;
            
            new_staff = {
                "id": auto_id,
                "name": name,
                "salary": float(salary)
            }
            staff_manager.append(new_staff);
            print(f"Thêm nhân viên thành công! ID: {auto_id}");
            auto_id += 1;
            
        case "2":
            if staff_manager == []:
                print("Chưa có nhân viên nào trong danh sách!");
                continue;
            header = f"{'ID':<5} | {'TÊN NHÂN VIÊN':<20} | {'MỨC LƯƠNG':<15}";
            print(header);
            print('-'*len(header));
            for staff in staff_manager:
                print(f"{staff['id']:<5} | {staff['name']:<20} | {staff['salary']:<15}");
        case "3":
            while True:
                id = input("Nhập id cần xóa: ").strip();
                if id:
                    break;
                print("Tên nhân viên không được để trống");
            temp_idx = -1
            for idx,staff in enumerate(staff_manager):
                if int(id) == staff["id"]:
                    temp_idx = idx;
                    break;
            if temp_idx == -1:
                print("Không tìm thấy nhân viên để xóa!");
                continue;
            del staff_manager[temp_idx];
            print(f"Đã xóa nhân viên ID {id} thành công!");
        case _:
            print("Lỗi lựa chọn vui lòng nhập lại!");