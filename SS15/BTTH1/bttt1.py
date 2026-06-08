# Khởi tạo các biến toàn cục quản lý trạng thái hệ thống
inventory_stock = 100
total_revenue = 0.0

def add_stock(amount):
    """
    Cập nhật số lượng sản phẩm nhập thêm vào kho.
    
    Args:
        amount (int): Số lượng sản phẩm cần thêm vào hệ thống.
    """
    global inventory_stock
    inventory_stock += amount
    print(f"Đã nhập thành công {amount} sản phẩm.")
    print(f"Tồn kho hiện tại: {inventory_stock}")


def process_sale(quantity):
    """
    Kiểm tra tình trạng hàng trong kho trước khi tiến hành giao dịch.
    
    Args:
        quantity (int): Số lượng sản phẩm khách hàng muốn mua.
        
    Returns:
        bool: True nếu kho đủ hàng, False nếu kho không đủ đáp ứng.
    """
    if inventory_stock >= quantity:
        return True
    else:
        print(f"Lỗi: Không đủ hàng trong kho. Tồn kho hiện tại chỉ còn {inventory_stock}.")
        return False


def calculate_final_price(quantity, price):
    """
    Tính toán chi phí đơn hàng, bao gồm chiết khấu và thuế VAT.
    """
    total = quantity * price
    discount = 0.0
    
    # Giảm 10% nếu tổng hóa đơn từ 1000 trở lên
    if total >= 1000:
        discount = total * 0.10
        
    total_after_discount = total - discount
    vat = total_after_discount * 0.08
    final_total = total_after_discount + vat
    
    print("-> Hóa đơn chi tiết:")
    print(f"Số lượng: {quantity} | Đơn giá: ${float(price)}")
    print(f"Tạm tính: ${float(total)}")
    if discount > 0:
        print(f"Giảm giá (10%): ${float(discount)}")
    print(f"Thuế VAT (8%): ${float(vat)}")
    print(f"Tổng thanh toán: ${float(final_total)}")
    
    return final_total


def print_report():
    """
    In báo cáo tổng quan về trạng thái kinh doanh và kho hàng.
    """
    print("--- BÁO CÁO KINH DOANH ---")
    print(f"Tồn kho hiện tại: {inventory_stock} sản phẩm")
    print(f"Tổng doanh thu: ${float(total_revenue)}")


def get_valid_input(prompt, is_float=False):
    """
    Hàm phụ trợ: Xử lý bẫy dữ liệu (Edge Cases).
    Ép kiểu an toàn, bắt lỗi nhập chữ và chặn số âm.
    """
    while True:
        try:
            user_input = input(prompt)
            # Ép kiểu float hoặc int tùy theo yêu cầu
            value = float(user_input) if is_float else int(user_input)
            
            if value <= 0:
                print("Dữ liệu nhập vào phải lớn hơn 0.")
            else:
                return value
        except ValueError:
            print("Lỗi: Dữ liệu không hợp lệ. Vui lòng nhập số.")


def main():
    global inventory_stock, total_revenue
    
    while True:
        print("\n========== TECHSTORE MANAGEMENT SYSTEM ==========")
        print("1. Nhập thêm hàng vào kho")
        print("2. Bán hàng (Tính toán hóa đơn)")
        print("3. Xem báo cáo tổng quan")
        print("4. Thoát chương trình")
        print("=================================================")
        
        choice = input("Chọn chức năng (1-4): ")
        
        # Sử dụng match case thay cho if-elif-else
        match choice:
            case '1':
                print("--- NHẬP HÀNG ---")
                amount = get_valid_input("Nhập số lượng sản phẩm muốn thêm: ", is_float=False)
                add_stock(amount)
                
            case '2':
                print("--- BÁN HÀNG ---")
                quantity = get_valid_input("Nhập số lượng mua: ", is_float=False)
                price = get_valid_input("Nhập đơn giá ($): ", is_float=True)
                
                # Kiểm tra kho trước khi tính tiền
                if process_sale(quantity):
                    # Tính toán ra số tiền cuối cùng cần thanh toán
                    final_total = calculate_final_price(quantity, price)
                    
                    # Trừ kho và cộng doanh thu sau khi giao dịch hợp lệ
                    inventory_stock -= quantity
                    total_revenue += final_total
                    print("Đã bán thành công!")
                    
            case '3':
                print_report()
                
            case '4':
                print("Đã thoát chương trình quản lý. Tạm biệt!")
                break
                
            case _:
                print("Lựa chọn không hợp lệ. Vui lòng nhập từ 1 đến 4.")

if __name__ == "__main__":
    main()