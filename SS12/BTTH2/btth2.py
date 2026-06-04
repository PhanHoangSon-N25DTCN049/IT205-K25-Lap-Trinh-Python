saving_accounts = [
    {"account_id": "STK001", "customer_name": "Nguyễn Văn An", "balance": 50000000, "term_months": 6, "interest_rate": 6.5, "status": "active"},
    {"account_id": "STK002", "customer_name": "Trần Thị Bình", "balance": 120000000, "term_months": 12, "interest_rate": 7.2, "status": "active"}
]

while True:
    print("\n=========================================================")
    print("     HỆ THỐNG QUẢN LÝ TÀI KHOẢN TIẾT KIỆM TECHBANK")
    print("=========================================================")
    print("  1. Xem danh sách sổ tiết kiệm")
    print("  2. Mở sổ tiết kiệm mới")
    print("  3. Cập nhật thông tin sổ tiết kiệm")
    print("  4. Tất toán hoặc xóa sổ tiết kiệm")
    print("  5. Tính lãi dự kiến khi đến hạn")
    print("  6. Kiểm tra điều kiện rút trước hạn")
    print("  7. Thoát chương trình")
    print("=========================================================")

    choice = input("Nhập lựa chọn của bạn (1-7): ").strip()

    match choice:
        case "7":
            break
            
        case "1":
            if not saving_accounts:
                print("Danh sách sổ tiết kiệm hiện đang trống")
            else:
                print("Danh sách sổ tiết kiệm:")
                for i, acc in enumerate(saving_accounts, 1):
                    print(f"{i}. Mã sổ: {acc['account_id']} | Khách hàng: {acc['customer_name']} | Số tiền gửi: {acc['balance']} | Kỳ hạn: {acc['term_months']} tháng | Lãi suất: {acc['interest_rate']}%/năm | Trạng thái: {acc['status']}")
                    
        case "2":
            acc_id = input("Nhập mã sổ tiết kiệm: ").replace(" ", "").upper()
            
            is_exist = False
            for acc in saving_accounts:
                if acc["account_id"] == acc_id:
                    is_exist = True
                    break
                    
            if is_exist:
                print("Mã sổ tiết kiệm đã tồn tại!")
                continue
                
            name = input("Nhập tên khách hàng: ").strip()
            if not name:
                print("Tên khách hàng không được để trống")
                continue
                
            balance_str = input("Nhập số tiền gửi: ").strip()
            term_str = input("Nhập kỳ hạn gửi theo tháng: ").strip()
            
            if not balance_str.isdigit() or not term_str.isdigit() or int(balance_str) <= 0 or int(term_str) <= 0:
                print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                continue
                
            rate_str = input("Nhập lãi suất năm: ").strip()
            try:
                rate = float(rate_str)
                if rate <= 0:
                    raise ValueError
            except ValueError:
                print("Lãi suất không hợp lệ!")
                continue
                
            new_account = {
                "account_id": acc_id,
                "customer_name": name,
                "balance": int(balance_str),
                "term_months": int(term_str),
                "interest_rate": rate,
                "status": "active"
            }
            saving_accounts.append(new_account)
            print("Mở sổ tiết kiệm thành công!")
            
        case "3":
            acc_id = input("Nhập mã sổ tiết kiệm cần cập nhật: ").replace(" ", "").upper()
            target_acc = None
            for acc in saving_accounts:
                if acc["account_id"] == acc_id:
                    target_acc = acc
                    break
                    
            if not target_acc:
                print("Không tìm thấy mã sổ tiết kiệm!")
                continue
                
            if target_acc["status"] == "closed":
                print("Không thể cập nhật sổ tiết kiệm đã tất toán!")
                continue
                
            name = input("Nhập tên khách hàng mới: ").strip()
            if not name:
                print("Tên khách hàng không được để trống")
                continue
                
            balance_str = input("Nhập số tiền gửi mới: ").strip()
            term_str = input("Nhập kỳ hạn mới theo tháng: ").strip()
            
            if not balance_str.isdigit() or not term_str.isdigit() or int(balance_str) <= 0 or int(term_str) <= 0:
                print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                continue
                
            rate_str = input("Nhập lãi suất năm mới: ").strip()
            try:
                rate = float(rate_str)
                if rate <= 0:
                    raise ValueError
            except ValueError:
                print("Lãi suất không hợp lệ!")
                continue
                
            target_acc["customer_name"] = name
            target_acc["balance"] = int(balance_str)
            target_acc["term_months"] = int(term_str)
            target_acc["interest_rate"] = rate
            print("Cập nhật thông tin sổ tiết kiệm thành công!")
            
        case "4":
            acc_id = input("Nhập mã sổ tiết kiệm cần tất toán/xóa: ").replace(" ", "").upper()
            target_acc = None
            for acc in saving_accounts:
                if acc["account_id"] == acc_id:
                    target_acc = acc
                    break
                    
            if not target_acc:
                print("Không tìm thấy mã sổ tiết kiệm!")
                continue
                
            if target_acc["status"] == "closed":
                print("Không thể thao tác với sổ tiết kiệm đã tất toán!")
                continue
                
            target_acc["status"] = "closed"
            print("Tất toán sổ thành công!")
            
        case "5":
            acc_id = input("Nhập mã sổ tiết kiệm cần tính lãi: ").replace(" ", "").upper()
            target_acc = None
            for acc in saving_accounts:
                if acc["account_id"] == acc_id:
                    target_acc = acc
                    break
                    
            if not target_acc:
                print("Không tìm thấy mã sổ tiết kiệm!")
                continue
                
            if target_acc["status"] == "closed":
                print("Không thể thao tác với sổ tiết kiệm đã tất toán!")
                continue
                
            interest = target_acc["balance"] * target_acc["interest_rate"] / 100 * target_acc["term_months"] / 12
            total = target_acc["balance"] + interest
            print(f"Tiền lãi dự kiến: {interest:,.0f} | Tổng tiền nhận: {total:,.0f}")
            
        case "6":
            acc_id = input("Nhập mã sổ tiết kiệm cần kiểm tra: ").replace(" ", "").upper()
            target_acc = None
            for acc in saving_accounts:
                if acc["account_id"] == acc_id:
                    target_acc = acc
                    break
                    
            if not target_acc:
                print("Không tìm thấy mã sổ tiết kiệm!")
                continue
                
            if target_acc["status"] == "closed":
                print("Không thể thao tác với sổ tiết kiệm đã tất toán!")
                continue
                
            months_str = input("Nhập số tháng thực gửi: ").strip()
            if not months_str.isdigit() or int(months_str) <= 0:
                print("Số tháng thực gửi không hợp lệ!")
                continue
                
            months_sent = int(months_str)
            rate = target_acc["interest_rate"] if months_sent >= target_acc["term_months"] else 0.5
            interest = target_acc["balance"] * rate / 100 * months_sent / 12
            total = target_acc["balance"] + interest
            print(f"Lãi suất áp dụng: {rate}%/năm. Tiền lãi thực nhận: {interest:,.0f} | Tổng tiền thực nhận: {total:,.0f}")
            
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại")