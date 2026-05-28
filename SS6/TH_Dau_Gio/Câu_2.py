total_err = 0;
while True:
    temp = int(input("Nhập số lượng hàng lỗi(-1 để kết thúc): "));
    if temp == -1:
        break;
    total_err += temp;
      
print("Tổng số lượng hàng lỗi trong ngày là: ", total_err);