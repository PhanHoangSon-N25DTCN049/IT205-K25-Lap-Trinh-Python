weekly_revenue = 0;
target_date = 0;
for count in range (7):
    temp = int(input(f"Nhập doanh thu ngày {count + 1}: "));
    weekly_revenue += temp;
    if temp >= 5000000:
        target_date = target_date + 1
    
avg_revenue = weekly_revenue / 7;
print(" --- BÁO CÁO DOANH THU TUẦN RIKKEI STORE --- ");
print(f"Tổng doanh thu tuần: {weekly_revenue} ");
print(f"Trung bình doanh thu tuần: {avg_revenue} ");
print(f"Ngày đạt chỉ tiêu doanh thu tuần: {target_date} ");

