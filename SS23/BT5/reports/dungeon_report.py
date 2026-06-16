from colorama import Fore, Style, init

# Khởi tạo thư viện bên thứ ba colorama để đổi màu sắc văn bản
init(autoreset=True)

def display_players(records):
    """
    Chức năng 1: Hiển thị danh sách người chơi kèm phân loại trạng thái HP.
    Bẫy 2: Kiểm tra danh sách người chơi rỗng.
    """
    if not records:
        print("Hệ thống chưa có dữ liệu người chơi.")
        return

    print("\n--- DANH SÁCH NGƯỜI CHƠI ---")
    for idx, player in enumerate(records, 1):
        hp = player["hp"]
        
        # Xác định trạng thái người chơi dựa theo khoảng HP quy định
        if hp <= 0:
            status = Fore.RED + "Đã gục ngã"
        elif hp < 50:
            status = Fore.YELLOW + "Nguy hiểm"
        elif hp < 100:
            status = Fore.CYAN + "Ổn định"
        else:
            status = Fore.GREEN + "Sung sức"

        print(f"{idx}. Mã: {player['player_id']} | Tên: {player['name']} | "
              f"HP: {hp} | Mana: {player['mana']} | Gold: {player['gold']} | "
              f"Level: {player['level']} | Trạng thái: {status}{Style.RESET_ALL}")
    print("------------------------------")


def show_leaderboard(records):
    """
    Chức năng 5: Hiển thị bảng xếp hạng người chơi không làm thay đổi danh sách gốc.
    Tiêu chí sắp xếp đa cấp độ: Level -> Gold -> HP.
    """
    if not records:
        print("Hệ thống chưa có dữ liệu người chơi.")
        return

    print("\n--- BẢNG XẾP HẠNG NGƯỜI CHƠI ---")
    # Sử dụng hàm sorted và lambda với bộ key giá trị âm để đảo ngược thứ tự giảm dần
    leaderboard = sorted(
        records, 
        key=lambda p: (-p["level"], -p["gold"], -p["hp"])
    )

    for idx, player in enumerate(leaderboard, 1):
        print(f"{idx}. {player['name']} | Level: {player['level']} | "
              f"Gold: {player['gold']} | HP: {player['hp']}")
    print("--------------------------------")