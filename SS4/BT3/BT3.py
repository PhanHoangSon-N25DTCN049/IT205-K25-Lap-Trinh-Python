total_bill = int(input("Nhập số lượng hóa đơn trong ca: "));
max_bill = 0;
min_bill = 1000000000000000000;
for i in range(total_bill):
    temp = int(input(f"Nhập hóa đơn thứ {i + 1}: "));
    if temp > max_bill:
        max_bill = temp;
    if temp < min_bill:
        min_bill = temp;

print("--- Kết quả kiểm toán ca RIKKEI STORE ---");
print(f"Hóa đơn có giá trị lớn nhất là: {max_bill}");
print(f"Hóa đơn có giá trị nhỏ nhất là: {min_bill}");