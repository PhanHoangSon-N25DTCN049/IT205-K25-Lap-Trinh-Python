import re

class MemberCard:
    # Class Attribute - Áp dụng chung cho toàn bộ hệ thống
    point_value_vnd = 1000

    def __init__(self, card_id, name):
        self.card_id = card_id
        self.name = name
        # Các thuộc tính private được bảo mật bằng Name Mangling
        self.__points = 0
        self.__tier = "Standard"

    # Getter cho thuộc tính __points (Chỉ đọc)
    @property
    def points(self):
        return self.__points

    # Getter cho thuộc tính __tier (Chỉ đọc)
    @property
    def tier(self):
        return self.__tier

    # Instance Method: Tích điểm khi khách mua hàng
    def earn_points(self, bill_amount):
        points_earned = int(bill_amount // 10000)
        self.__points += points_earned
        
        print(f"\nKhách hàng: {self.name}")
        print(f"Hóa đơn: {bill_amount:,} VNĐ")
        print(f"Số điểm được tích: {points_earned}")
        print(f"Tổng điểm hiện tại: {self.__points}")
        
        # Tự động thăng hạng lên VIP nếu đủ điều kiện
        if self.__points >= 100 and self.__tier != "VIP":
            self.__tier = "VIP"
            print("\nChúc mừng! Khách hàng đã được nâng hạng lên VIP.")
            
        print(f"Hạng thẻ hiện tại: {self.__tier}")

    # Instance Method: Tiêu điểm đổi ưu đãi
    def redeem_points(self, points_to_use):
        if points_to_use <= 0:
            print("\nSố điểm sử dụng phải lớn hơn 0!")
            return False
            
        if points_to_use > self.__points:
            print("\nKhông thể đổi điểm!")
            print("Số điểm muốn sử dụng vượt quá số điểm hiện có.")
            print(f"Điểm hiện tại của khách: {self.__points}")
            print(f"Số điểm sau giao dịch: {self.__points}")
            return False

        # Sử dụng Class Attribute để tính tiền giảm giá
        discount_amount = points_to_use * MemberCard.point_value_vnd
        self.__points -= points_to_use
        
        print(f"\nĐã trừ {points_to_use} điểm.")
        print(f"Khách hàng được giảm giá {discount_amount:,} VNĐ vào hóa đơn!")
        print(f"Số điểm còn lại: {self.__points}")
        print(f"Hạng thẻ hiện tại: {self.__tier}")
        return True

    # Class Method: Cập nhật tỷ giá hệ thống
    @classmethod
    def update_point_value(cls, new_value):
        if new_value > 0:
            cls.point_value_vnd = new_value
            print("\nCập nhật tỷ giá thành công!")
            print(f"Tỷ giá mới: 1 điểm = {cls.point_value_vnd:,} VNĐ")
        else:
            print("\nTỷ giá quy đổi mới phải lớn hơn 0!")

    # Static Method: Kiểm tra định dạng mã thẻ trước khi khởi tạo
    @staticmethod
    def is_valid_card_id(card_id):
        # Định dạng chuẩn: Bắt đầu bằng 'RC' hoa và theo sau là đúng 2 chữ số
        return bool(re.match(r"^RC\d{2}$", card_id))


# --- CHƯƠNG TRÌNH ĐIỀU KHIỂN CHÍNH (MAIN FLOW WITH MATCH-CASE) ---
def main():
    cards_database = [
        MemberCard("RC01", "Nguyen Van A"),
        MemberCard("RC02", "Tran Thi B")
    ]
    
    # Khởi tạo dữ liệu demo ban đầu
    cards_database[0].earn_points(1500000)
    cards_database[1].earn_points(200000)

    while True:
        print("\n===== HỆ THỐNG THẺ THÀNH VIÊN RIKKEI COFFEE =====")
        print("1. Xem danh sách thẻ thành viên")
        print("2. Đăng ký thẻ mới")
        print("3. Khách mua hàng (Tích điểm)")
        print("4. Khách dùng điểm (Đổi ưu đãi)")
        print("5. Cập nhật tỷ giá quy đổi điểm (Hệ thống)")
        print("6. Thoát chương trình")
        print("======================================================")
        
        choice = input("Chọn chức năng (1-6): ").strip()
        
        match choice:
            case "1":
                print("\n--- DANH SÁCH THẺ THÀNH VIÊN ---")
                if not cards_database:
                    print("Hệ thống chưa có thẻ thành viên nào.")
                else:
                    for idx, card in enumerate(cards_database, 1):
                        print(f"{idx}. Mã: {card.card_id} | Tên: {card.name:<15} | Điểm: {card.points:<3} | Hạng: {card.tier}")
                        
            case "2":
                print("\n--- ĐĂNG KÝ THẺ THÀNH VIÊN MỚI ---")
                card_id = input("Nhập mã thẻ: ").strip()
                
                if not MemberCard.is_valid_card_id(card_id):
                    print("\nMã thẻ không hợp lệ! Định dạng chuẩn phải là RCxx (ví dụ: RC03, RC99).")
                    continue
                    
                if any(card.card_id == card_id for card in cards_database):
                    print("\nMã thẻ đã tồn tại trong hệ thống!\nVui lòng kiểm tra lại.")
                    continue
                    
                name = input("Nhập tên khách hàng: ").strip().title()
                new_card = MemberCard(card_id, name)
                cards_database.append(new_card)
                
                print("\nĐăng ký thẻ thành viên thành công!")
                print(f"Mã thẻ: {new_card.card_id} | Tên: {new_card.name} | Hạng: {new_card.tier}")
                
            case "3":
                print("\n--- KHÁCH MUA HÀNG - TÍCH ĐIỂM ---")
                card_id = input("Nhập mã thẻ: ").strip()
                
                card = next((c for c in cards_database if c.card_id == card_id), None)
                if not card:
                    print("\nKhông tìm thấy mã thẻ này trong hệ thống!")
                    continue
                    
                try:
                    bill_amount = float(input("Nhập tổng tiền hóa đơn: "))
                    if bill_amount <= 0:
                        print("Số tiền hóa đơn phải lớn hơn 0 VNĐ!")
                        continue
                    card.earn_points(bill_amount)
                except ValueError:
                    print("Vui lòng nhập số tiền hóa đơn hợp lệ!")
                    
            case "4":
                print("\n--- KHÁCH DÙNG ĐIỂM - ĐỔI ƯU ĐÃI ---")
                print(f"Tỷ giá hiện tại là: 1 điểm = {MemberCard.point_value_vnd:,} VNĐ")
                card_id = input("Nhập mã thẻ: ").strip()
                
                card = next((c for c in cards_database if c.card_id == card_id), None)
                if not card:
                    print("\nKhông tìm thấy mã thẻ này trong hệ thống!")
                    continue
                    
                try:
                    points_to_use = int(input("Nhập số điểm muốn sử dụng: "))
                    card.redeem_points(points_to_use)
                except ValueError:
                    print("Vui lòng nhập số điểm nguyên hợp lệ!")
                    
            case "5":
                print("\n--- CẬP NHẬT TỶ GIÁ QUY ĐỔI ĐIỂM ---")
                print(f"Tỷ giá hiện tại: 1 điểm = {MemberCard.point_value_vnd:,} VNĐ")
                try:
                    new_rate = int(input("Nhập tỷ giá mới cho 1 điểm: "))
                    MemberCard.update_point_value(new_rate)
                except ValueError:
                    print("Vui lòng nhập số nguyên hợp lệ!")
                    
            case "6":
                print("\nCảm ơn bạn đã sử dụng hệ thống thẻ thành viên Rikkei Coffee!")
                break
                
            case _:
                print("\nChức năng không hợp lệ! Vui lòng chọn từ 1 đến 6.")

if __name__ == "__main__":
    main()