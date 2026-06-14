
# (1) TÀI LIỆU PHÂN TÍCH THIẾT KẾ (CLEAN CODE & LOGIC REPORT)
# 
# 1. Khắc phục lỗi Logic ẩn (Chức năng 5 - Báo cáo doanh thu):
#    - Vấn đề: Code cũ cộng dồn tất cả các vé mà không kiểm tra trạng thái, 
#      dẫn đến việc tính cả tiền của những vé đã bị hủy ("Cancelled").
#    - Giải pháp (Đã Debug): Thêm câu lệnh điều kiện `if ticket.get("status") == "Booked"` 
#      vào trong vòng lặp tính toán để hệ thống chỉ ghi nhận doanh thu từ các vé hợp lệ.
# 
# 2. Cơ chế xử lý Tuple Chỗ Ngồi (Chức năng 3):
#    - Vì Tuple trong Python là kiểu dữ liệu Immutable (không thể chỉnh sửa phần tử), 
#      việc ghi trực tiếp dạng `ticket["seat"][1] = new_number` sẽ ném ra lỗi TypeError.
#    - Giải pháp Clean Code: Tiến hành tạo một bộ Tuple mới hoàn toàn từ dữ liệu 
#      trọng tài nhập vào: `(new_zone, new_seat_num)` rồi ghi đè lên key "seat".
# ==============================================================================

import logging

# Cấu hình logging ghi vết hệ thống vào file arena_tickets.log
logging.basicConfig(
    filename='arena_tickets.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Khởi tạo cơ sở dữ liệu vé mẫu (Mock Data)
ticket_db = [
    {"ticket_id": "T01", "buyer_name": "Nguyen Van A", "price": 500.0, "status": "Booked", "seat": ("A", 1)},
    {"ticket_id": "T02", "buyer_name": "Tran Thi B", "price": 300.0, "status": "Cancelled", "seat": ("B", 5)},
    {"ticket_id": "T03", "buyer_name": "Le Van C", "price": 500.0, "status": "Booked", "seat": ("A", 2)}
]

def calculate_total_revenue(ticket_list: list) -> float:
    """
    [Helper Function] Tính toán tổng doanh thu hợp lệ từ danh sách vé.
    Chỉ cộng tiền các vé có trạng thái 'Booked'. Ném ra KeyError nếu thiếu trường 'price'.
    """
    total = 0.0
    for ticket in ticket_list:
        if ticket.get("status") == "Booked":
            total += float(ticket["price"])  # Có thể ném KeyError nếu thiếu key 'price'
    return total

def display_tickets(tickets: list) -> None:
    """Chức năng 1: Xem danh sách vé đã bán"""
    if not tickets:
        print("\nHiện chưa có vé nào trong hệ thống.")
        logging.info("User viewed ticket list.")
        return

    print("\n--- DANH SÁCH VÉ ---")
    print(f"{'Mã Vé':<6} | {'Tên Khách Hàng':<16} | {'Giá Vé':<8} | {'Chỗ Ngồi':<8} | Trạng Thái")
    print("-" * 60)
    
    for t in tickets:
        try:
            t_id = t["ticket_id"]
            name = t["buyer_name"]
            price = t["price"]
            status = t["status"]
            seat_tuple = t["seat"]  # Trích xuất bộ tuple chỗ ngồi
            seat_str = f"{seat_tuple[0]}-{seat_tuple[1]}"
            
            # Đánh dấu cấu trúc nếu vé đã bị hủy
            display_status = status
            if status == "Cancelled":
                display_status += " [ĐÃ HỦY]"
                
            print(f"{t_id:<6} | {name:<16} | {price:<8.1f} | {seat_str:<8} | {display_status}")
        except KeyError as e:
            print("-" * 60)
            print(f"Lỗi: Một vé đang bị thiếu dữ liệu, vui lòng kiểm tra lại.")
            print("-" * 60)
            logging.error(f"Missing key while displaying ticket: {e}")
            return
            
    print("-" * 60)
    logging.info("User viewed ticket list.")

def book_ticket(tickets: list) -> None:
    """Chức năng 2: Đặt vé mới"""
    print("\n--- ĐẶT VÉ MỚI ---")
    ticket_id = input("Nhập mã vé: ").strip().upper()
    
    if not ticket_id:
        print("Mã vé không được để trống!")
        return

    # Bẫy trùng ID vé
    for t in tickets:
        if t["ticket_id"] == ticket_id:
            print(f"Lỗi: Mã vé {ticket_id} đã tồn tại.")
            logging.warning(f"Duplicate ticket ID entered: {ticket_id}")
            return

    buyer_name = input("Nhập tên khách hàng: ").strip()
    
    # Bẫy lỗi nhập giá vé (Phải là số và > 0)
    while True:
        try:
            price_input = input("Nhập giá vé: ").strip()
            price = float(price_input)
            if price <= 0:
                print("\nGiá vé phải lớn hơn 0. Vui lòng nhập lại.")
                continue
            break
        except ValueError:
            print("\nGiá vé phải là số. Vui lòng nhập lại.")
            logging.warning("Invalid price input while booking ticket")

    zone = input("Nhập khu vực ghế: ").strip().upper()
    
    # Bẫy lỗi nhập số ghế (Phải là số nguyên dương)
    while True:
        try:
            seat_num_input = input("Nhập số ghế: ").strip()
            seat_num = int(seat_num_input)
            if seat_num <= 0:
                print("\nSố ghế phải lớn hơn 0. Vui lòng nhập lại.")
                continue
            break
        except ValueError:
            print("\nSố ghế phải là số nguyên. Vui lòng nhập lại.")

    # Đóng gói tạo tuple seat trước khi lưu vào dictionary theo yêu cầu nghiệp vụ
    new_ticket = {
        "ticket_id": ticket_id,
        "buyer_name": buyer_name,
        "price": price,
        "status": "Booked",
        "seat": (zone, seat_num)
    }
    
    tickets.append(new_ticket)
    print(f"\nThành công: Đã đặt vé {ticket_id} cho khách hàng {buyer_name}.")
    logging.info(f"Booked new ticket {ticket_id} for {buyer_name}")

def change_seat(tickets: list) -> None:
    """Chức năng 3: Đổi chỗ ngồi (Cập nhật vé)"""
    print("\n--- ĐỔI CHỖ NGỒI ---")
    ticket_id = input("Nhập mã vé cần đổi chỗ: ").strip().upper()
    
    target_ticket = None
    for t in tickets:
        if t["ticket_id"] == ticket_id:
            target_ticket = t
            break
            
    if not target_ticket:
        print(f"\nKhông tìm thấy vé mang mã {ticket_id}.")
        logging.warning(f"Change seat failed - Ticket {ticket_id} not found")
        return

    new_zone = input("Nhập khu vực ghế mới: ").strip().upper()
    
    # Bẫy lỗi nhập số ghế mới
    while True:
        try:
            seat_input = input("Nhập số ghế mới: ").strip()
            new_seat_num = int(seat_input)
            if new_seat_num <= 0:
                print("\nSố ghế phải lớn hơn 0. Vui lòng nhập lại.")
                continue
            break
        except ValueError:
            print("\nSố ghế phải là số nguyên. Vui lòng nhập lại.")

    # Xử lý cốt lõi: Ghi đè Tuple hoàn toàn mới để tránh lỗi định dạng dữ liệu tuple tĩnh
    target_ticket["seat"] = (new_zone, new_seat_num)
    print(f"\nThành công: Đã đổi chỗ vé {ticket_id} sang {new_zone}-{new_seat_num}.")
    logging.info(f"Seat changed for ticket {ticket_id} to {new_zone}-{new_seat_num}")

def cancel_ticket(tickets: list) -> None:
    """Chức năng 4: Hủy vé"""
    print("\n--- HỦY VÉ ---")
    ticket_id = input("Nhập mã vé cần hủy: ").strip().upper()
    
    target_ticket = None
    for t in tickets:
        if t["ticket_id"] == ticket_id:
            target_ticket = t
            break
            
    if not target_ticket:
        print(f"\nKhông tìm thấy vé mang mã {ticket_id}.")
        logging.warning(f"Cancel ticket failed - Ticket {ticket_id} not found")
        return

    if target_ticket["status"] == "Cancelled":
        print(f"\nVé {ticket_id} đã ở trạng thái Cancelled trước đó.")
        return

    target_ticket["status"] = "Cancelled"
    print(f"\nThành công: Vé {ticket_id} đã được hủy.")
    logging.warning(f"Ticket {ticket_id} has been cancelled.")

def generate_revenue_report(tickets: list) -> None:
    """Chức năng 5: Báo cáo doanh thu (Đã qua xử lý debug)"""
    print("\n--- BÁO CÁO DOANH THU ---")
    
    booked_count = sum(1 for t in tickets if t.get("status") == "Booked")
    cancelled_count = sum(1 for t in tickets if t.get("status") == "Cancelled")
    
    try:
        # Gọi hàm phụ trợ đã bẫy lỗi loại bỏ vé hủy
        total_revenue = calculate_total_revenue(tickets)
        print(f"Tổng số vé đã đặt: {booked_count}")
        print(f"Tổng số vé đã hủy: {cancelled_count}")
        print(f"Tổng doanh thu hợp lệ: {total_revenue:,}.0")
        logging.info(f"Revenue report generated. Total: {total_revenue}")
    except KeyError as e:
        print("Lỗi: Một vé đang bị thiếu dữ liệu doanh thu.")
        print("Tổng doanh thu hợp lệ: 0.0")
        logging.error(f"Missing key while calculating revenue: {e}")

def main():
    """Điều hướng luồng chạy menu sử dụng cấu trúc case mặc định"""
    while True:
        print("\n=== HỆ THỐNG QUẢN LÝ VÉ RIKKEI ESPORTS ===")
        print("1. Xem danh sách vé đã bán")
        print("2. Đặt vé mới")
        print("3. Đổi chỗ ngồi (Cập nhật vé)")
        print("4. Hủy vé")
        print("5. Báo cáo doanh thu")
        print("6. Thoát chương trình")
        print("========================================")
        
        choice = input("Chọn chức năng (1-6): ").strip()
        
        match choice:
            case "1":
                display_tickets(ticket_db)
            case "2":
                book_ticket(ticket_db)
            case "3":
                change_seat(ticket_db)
            case "4":
                cancel_ticket(ticket_db)
            case "5":
                generate_revenue_report(ticket_db)
            case "6":
                print("\nCảm ơn bạn đã sử dụng hệ thống quản lý vé Rikkei Esports.")
                logging.info("Ticket management system closed.")
                break
            case _:
                print("\nLựa chọn không hợp lệ! Vui lòng chọn lại từ 1 đến 6.")

if __name__ == "__main__":
    main()