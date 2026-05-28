stock = int(input("Nhập số hàng tồn kho của hàng: "));
if stock >= 50:
    print('Tình trạng: Hàng đầy kho');
elif stock >= 10 and stock < 50:
    print("Tình trạng: Mức an toàn");
elif stock < 10:
    print("Tình trạng: Sắp hết hàng, cần báo cáo nhập thêm");
    
