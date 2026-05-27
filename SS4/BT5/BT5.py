count = 1;
total_invoice_value = 0;
invoices_meet_targets = 0;
choice = 'C';
while choice != 'K':
    invoice_value = int(input(f"Khách hàng {count} - Nhập giá trị hóa đơn: "));
    total_invoice_value += invoice_value;
    choice = input("Có muốn nhập tiếp không (C/K): ");
    if choice == 'C':
        count += 1;
    if invoice_value >= 1000000:
        invoices_meet_targets += 1;
        
print(" -- BÁO CÁO DOANH THU CUỐI NGÀY RIKKEI STORE --");
print(f"Tổng số hóa đơn đã xử lý: {count} hóa đơn");
print(f"Tổng doanh thu hôm nay: {total_invoice_value} VND");
print(f"Tổng số hóa đơn đạt mục tiêu (>= 1000000 VND): {invoices_meet_targets}");
print(f"Tỉ lệ hóa đơn lớn đạt: {invoices_meet_targets / count * 100}%  Trên tổng số đơn hàng");