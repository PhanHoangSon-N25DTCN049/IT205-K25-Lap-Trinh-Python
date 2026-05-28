ton_kho = 100;
while True:
    xuat = int(input("Nhập số lượng hàng xuất: "));
    if xuat < 0:
        print("Không được nhập số âm, vui lòng nhập lại");
        continue;
    elif xuat > ton_kho:
        print("Kho không đủ hàng, vui lòng nhập lại!");
        continue;
    ton_kho -= xuat;
    print("Xuất kho thành công!");
    print("Tồn kho còn lại: ", ton_kho);
    break;