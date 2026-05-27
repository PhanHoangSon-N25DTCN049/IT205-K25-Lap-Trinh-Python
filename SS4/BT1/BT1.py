initial_total_amount = int(input("Tổng tiền hóa đơn ban đầu: "));

print(" --- HÓA ĐƠN THANH TOÁN RIKKEI STORE --- ");
if initial_total_amount >= 500000:
    discount_amount = initial_total_amount * 0.1;

final_total_amount = initial_total_amount - discount_amount;
print(f"Số tiền được giảm giá: {discount_amount} VND ");
print(f"Tổng tiền khách phải trả: {final_total_amount} VND");