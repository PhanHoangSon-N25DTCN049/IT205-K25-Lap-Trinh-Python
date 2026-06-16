import random
from utils.player_utils import find_player

# Danh sách vật phẩm trong cửa hàng theo yêu cầu đề bài
shop_items = {
    "Potion": 50,
    "Iron Sword": 200,
    "Magic Book": 300,
    "Mana Stone": 150
}

def open_treasure_chest(records):
    """
    Chức năng 2: Mở rương báu ngẫu nhiên sử dụng thư viện chuẩn random.
    """
    if not records:
        print("Hệ thống chưa có dữ liệu người chơi.")
        return

    pid = input("Nhập mã người chơi mở rương: ")
    idx = find_player(records, pid)
    
    if idx == -1:
        print("Không tìm thấy người chơi!")
        return

    player = records[idx]
    rewards = ["Potion", "Iron Sword", "Magic Scroll", "100 Gold", "Mana Stone"]
    gift = random.choice(rewards)

    print(f">> Người chơi {player['name']} đã mở rương!")
    print(f">> Phần thưởng nhận được: {gift}")

    if gift == "100 Gold":
        player["gold"] += 100
    else:
        player["inventory"].append(gift)
        print(f">> Đã thêm {gift} vào túi đồ.")


def buy_item(records):
    """
    Chức năng 3: Mua vật phẩm trong cửa hàng.
    Kiểm tra bẫy vật phẩm không tồn tại (Bẫy 3) và không đủ vàng (Bẫy 4).
    """
    if not records:
        print("Hệ thống chưa có dữ liệu người chơi.")
        return

    pid = input("Nhập mã người chơi: ")
    idx = find_player(records, pid)
    
    if idx == -1:
        print("Không tìm thấy người chơi!")
        return

    player = records[idx]
    item_name = input("Nhập tên vật phẩm muốn mua: ").strip()

    # Bẫy 3: Vật phẩm không tồn tại trong cửa hàng
    if item_name not in shop_items:
        print("Vật phẩm không tồn tại trong cửa hàng!")
        return

    item_cost = shop_items[item_name]

    # Bẫy 4: Không đủ vàng
    if player["gold"] < item_cost:
        print("Không đủ vàng để mua vật phẩm này!")
        return

    # Tiến hành trừ tiền và thêm đồ vào kho
    player["gold"] -= item_cost
    player["inventory"].append(item_name)
    print(f">> Mua thành công {item_name}!")
    print(f">> Số vàng còn lại: {player['gold']}")