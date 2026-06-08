# Khởi tạo các biến toàn cục (Global Variables)
available_seats = 50
flight_revenue = 0.0
BASE_PRICE = 2000.0
MAX_CAPACITY = 50

def calculate_cost(ticket_class, quantity):
    """
    Tính toán tổng chi phí mua vé máy bay bao gồm thuế phí.
    
    Args:
        ticket_class (int): Hạng vé (1 cho Economy, 2 cho Business).
        quantity (int): Số lượng vé cần mua.
        
    Returns:
        float: Tổng tiền thanh toán cuối cùng (đã cộng 5% phí dịch vụ).
    """
    price_per_ticket = BASE_PRICE if ticket_class == 1 else BASE_PRICE * 1.5
    subtotal = price_per_ticket * quantity
    total_payment = subtotal * 1.05
    
    return float(total_payment)


def process_booking(ticket_class, quantity, total_payment):
    """
    Xử lý logic đặt vé, kiểm tra ghế trống và cập nhật doanh thu toàn cục.
    """
    global available_seats, flight_revenue
    
    # Bẫy 1 - Overbooking: Kiểm tra số lượng ghế trống
    if quantity > available_seats:
        print(f"Rất tiếc, chuyến bay chỉ còn {available_seats} chỗ trống.")
        return False
        
    # Giao dịch hợp lệ: Tiến hành trừ ghế và cộng tiền
    available_seats -= quantity
    flight_revenue += total_payment
    
    # Tính toán lại chi tiết để in hóa đơn
    class_name = "Economy" if ticket_class == 1 else "Business"
    price_per_ticket = BASE_PRICE if ticket_class == 1 else BASE_PRICE * 1.5
    subtotal = price_per_ticket * quantity
    service_fee = subtotal * 0.05
    
    print("-> Xác nhận đặt chỗ:")
    print(f"Số lượng: {quantity} | Hạng: {class_name}")
    print(f"Tạm tính: ${float(subtotal)}")
    print(f"Phí dịch vụ (5%): ${float(service_fee)}")
    print(f"Tổng thanh toán: ${float(total_payment)}")
    print(f"Đặt vé thành công! Ghế trống còn lại: {available_seats}")
    return True


def process_refund(quantity):
    """
    Xử lý logic hủy vé, kiểm tra tính hợp lệ và hoàn tiền.
    """
    global available_seats, flight_revenue
    
    # Bẫy 2 - Ghost Refund: Ngăn chặn việc hủy số vé lớn hơn số vé đã bán
    if available_seats + quantity > MAX_CAPACITY:
        print("Lỗi: Số lượng vé hủy vượt quá số vé đã bán ra.")
        return 0.0
        
    # Logic hoàn tiền: 80% giá vé cơ bản
    refund_amount = (BASE_PRICE * 0.8) * quantity
    
    # Cập nhật hệ thống
    available_seats += quantity
    flight_revenue -= refund_amount
    
    return float(refund_amount)


def display_flight_status():
    """
    In báo cáo tình trạng chuyến bay VN2026.
    
    Định dạng báo cáo bao gồm:
    - Sức chứa tối đa của máy bay
    - Số lượng ghế đã được đặt thực tế
    - Số lượng ghế còn trống
    - Tổng doanh thu hiện tại (đã xử lý cộng/trừ từ các giao dịch)
    """
    booked_seats = MAX_CAPACITY - available_seats
    print("--- TÌNH TRẠNG CHUYẾN BAY VN2026 ---")
    print(f"Sức chứa tối đa: {MAX_CAPACITY}")
    print(f"Ghế đã đặt: {booked_seats}")
    print(f"Ghế trống: {available_seats}")
    print(f"Tổng doanh thu hiện tại: ${float(flight_revenue)}")


def get_valid_quantity(prompt):
    """
    Hàm phụ trợ: Xử lý Bẫy 3 - Ngăn chặn người dùng nhập chữ hoặc số âm/số 0.
    """
    while True:
        try:
            val = int(input(prompt))
            if val <= 0:
                print("Lỗi: Số lượng phải lớn hơn 0.")
            else:
                return val
        except ValueError:
            print("Lỗi: Vui lòng nhập một số nguyên hợp lệ.")


def main():
    """
    Hàm khởi chạy vòng lặp chính của hệ thống CLI.
    """
    while True:
        print("\n============= SKYBOOKING SYSTEM =============")
        print("Chuyến bay: VN2026 | Khởi hành: Hà Nội")
        print("1. Đặt vé máy bay")
        print("2. Hủy vé & Hoàn tiền")
        print("3. Xem tình trạng chuyến bay")
        print("4. Đóng hệ thống")
        print("=============================================")
        
        choice = input("Chọn chức năng (1-4): ")
        
        match choice:
            case '1':
                print("--- ĐẶT VÉ MÁY BAY ---")
                quantity = get_valid_quantity("Nhập số lượng vé: ")
                
                # Bẫy 3 - Chặn nhập sai hạng vé
                while True:
                    try:
                        t_class = int(input("Chọn hạng vé (1: Economy, 2: Business): "))
                        if t_class in [1, 2]:
                            break
                        print("Lỗi: Hạng vé không hợp lệ. Vui lòng chọn 1 hoặc 2.")
                    except ValueError:
                        print("Lỗi: Vui lòng nhập số 1 hoặc 2.")
                        
                # Luồng dữ liệu: Tính tiền -> Gửi tổng tiền sang hàm xử lý đặt vé
                total_payment = calculate_cost(t_class, quantity)
                process_booking(t_class, quantity, total_payment)
                
            case '2':
                print("--- HỦY VÉ & HOÀN TIỀN ---")
                quantity = get_valid_quantity("Nhập số lượng vé muốn hủy: ")
                
                refund_amount = process_refund(quantity)
                # Chỉ in thông báo thành công nếu hàm hoàn tiền trả về giá trị lớn hơn 0
                if refund_amount > 0:
                    print(f"Hủy vé thành công. Hệ thống đã hoàn lại: ${refund_amount} (80% giá cơ bản).")
                    print(f"Ghế trống hiện tại: {available_seats}")
                    
            case '3':
                display_flight_status()
                
            case '4':
                print("Đã đóng hệ thống. Tạm biệt!")
                break
                
            case _:
                print("Lựa chọn không hợp lệ. Vui lòng nhập từ 1 đến 4.")


if __name__ == "__main__":
    main()