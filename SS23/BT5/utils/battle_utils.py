import random
from utils.player_utils import find_player

monsters = [
    {"name": "Bug Python", "damage": 20, "reward_gold": 100},
    {"name": "Import Error", "damage": 35, "reward_gold": 150},
    {"name": "Module Not Found", "damage": 50, "reward_gold": 250}
]

def fight_monster(records):
    """
    Chức năng 4: Chiến đấu với quái vật ngẫu nhiên.
    Kiểm tra bẫy trạng thái người chơi đã gục ngã (Bẫy 5).
    """
    if not records:
        print("Hệ thống chưa có dữ liệu người chơi.")
        return

    pid = input("Nhập mã người chơi chiến đấu: ")
    idx = find_player(records, pid)
    
    if idx == -1:
        print("Không tìm thấy người chơi!")
        return

    player = records[idx]

    # Bẫy 5: Người chơi đã gục ngã (hp <= 0)
    if player["hp"] <= 0:
        print("Người chơi đã gục ngã, không thể tiếp tục chiến đấu!")
        return

    monster = random.choice(monsters)
    print(f">> Quái vật xuất hiện: {monster['name']}")
    
    # Thực hiện trừ máu người chơi theo sát thương quái vật
    player["hp"] -= monster["damage"]
    print(f">> {player['name']} bị mất {monster['damage']} HP.")

    if player["hp"] > 0:
        player["gold"] += monster["reward_gold"]
        print(f">> Chiến thắng! Bạn nhận được {monster['reward_gold']} vàng.")
        print(f">> HP còn lại: {player['hp']}")
    else:
        player["hp"] = 0  # Đảm bảo HP không bị âm
        print(">> Bạn đã thất bại và gục ngã trước quái vật!")