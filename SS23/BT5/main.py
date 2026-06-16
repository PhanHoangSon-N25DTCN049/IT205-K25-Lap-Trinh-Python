from data.players import player_records
from utils.item_utils import open_treasure_chest, buy_item
from utils.battle_utils import fight_monster
import reports.dungeon_report as dr  # Sử dụng alias import nâng cao

def main():
    while True:
        print("\n===== RIKKEI DUNGEON - PYTHON MODULE ADVENTURE =====")
        print("1. Hiển thị danh sách người chơi")
        print("2. Mở rương báu ngẫu nhiên")
        print("3. Mua vật phẩm trong cửa hàng")
        print("4. Chiến đấu với quái vật")
        print("5. Xem bảng xếp hạng người chơi")
        print("6. Thoát chương trình")
        print("====================================================")
        
        # Kiểm tra dữ liệu nhập menu hợp lệ, bẫy lỗi gõ ký tự lạ
        try:
            choice = int(input("Chọn chức năng (1-6): "))
        except ValueError:
            print("Chức năng không hợp lệ. Vui lòng nhập số nguyên từ 1 đến 6.")
            continue

        # Điều hướng xử lý mặc định dùng cấu trúc rẽ nhánh case
        match choice:
            case 1:
                dr.display_players(player_records)
            case 2:
                open_treasure_chest(player_records)
            case 3:
                buy_item(player_records)
            case 4:
                fight_monster(player_records)
            case 5:
                dr.show_leaderboard(player_records)
            case 6:
                print("Cảm ơn bạn đã tham gia Rikkei Dungeon!")
                break
            case _:
                print("Chức năng không hợp lệ. Vui lòng chọn số từ 1 đến 6.")

if __name__ == "__main__":
    main()