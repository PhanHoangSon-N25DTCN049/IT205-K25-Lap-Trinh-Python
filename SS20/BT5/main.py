
# 1. Quản lý ngoại lệ (Exception Handling):
#    - Chức năng 2 & 3: Bẫy lỗi nhập số lượng Fan Token bằng try...except ValueError. 
#      Nếu nhập chữ hoặc số thực, hệ thống ép nhập lại. Kiểm tra số nguyên dương (> 0).
#    - Chức năng 4: Bẫy lỗi nhập hệ số phong độ. Đảm bảo hệ số là kiểu float và ép 
#      giới hạn chặt chẽ trong khoảng [0.5 - 2.5] theo quy định nghiệp vụ.
#    - Chức năng 5: Bẫy lỗi nhập điểm gốc của trận đấu (Base points phải là số nguyên dương).
# 
# 2. Xử lý Edge Cases & Mã rác:
#    - Bẫy mã rác: Sử dụng .strip().upper() để chuẩn hóa mọi ID đầu vào (ví dụ: " gen01 " -> "GEN01").
#    - Tràn viền / Thiếu key: Sử dụng dict.get(key, default) để lấy dữ liệu an toàn, 
#      tránh KeyError nếu API trả về thiếu trường thông tin.
#    - Bẫy lỗi logic ẩn (Rút vốn): Khấu trừ đúng 10% phí giao dịch khi rút vốn, 
#      đảm bảo chỉ trừ số lượng token yêu cầu trong quỹ hệ thống và tính toán đúng số thực nhận về ví.
# ==============================================================================

import logging

# Cấu hình thư viện logging ghi file theo format chuẩn hệ thống
logging.basicConfig(
    filename='fantasy_league.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Khởi tạo danh sách dữ liệu tuyển thủ Fantasy ban đầu
players = [
    {
        "player_id": "T101",
        "name": "Faker",
        "market_value": 5000,
        "fan_tokens": 1500,
        "match_points": 0,
        "form_multiplier": 1.0
    },
    {
        "player_id": "GEN01",
        "name": "Chovy",
        "market_value": 4800,
        "fan_tokens": 800,
        "match_points": 500,
        "form_multiplier": 1.2
    },
    {
        "player_id": "DRX01",
        "name": "Deft",
        "market_value": 3000,
        "fan_tokens": 0,
        "match_points": 0,
        "form_multiplier": 0.8
    }
]

def find_player_by_id(player_list: list, player_id: str) -> int:
    """
    [Helper Function] Tìm kiếm tuyển thủ theo ID.
    @param player_list: Danh sách chứa các dictionary tuyển thủ.
    @param player_id: Mã định danh tuyển thủ cần tìm.
    @return: Vị trí index trong mảng nếu tìm thấy, ngược lại trả về -1.
    """
    standard_id = player_id.strip().upper()
    for index, player in enumerate(player_list):
        if player.get("player_id", "").strip().upper() == standard_id:
            return index
    return -1

def calc_actual_withdrawal(withdraw_amount: int) -> float:
    """
    [Helper Function] Tính số token thực nhận sau khi trừ phí giao dịch 10%.
    @param withdraw_amount: Số token muốn rút (phải là số nguyên dương).
    @return: Số token thực nhận sau khi khấu trừ.
    @raise ValueError: Nếu số token rút không hợp lệ (<= 0).
    """
    if withdraw_amount <= 0:
        raise ValueError("Số token rút phải là số nguyên dương.")
    return float(withdraw_amount * 0.9)

def display_market(player_list: list) -> None:
    """Chức năng 1: Xem Sàn Giao Dịch Tuyển Thủ"""
    if not player_list:
        print("\nSàn giao dịch hiện chưa có tuyển thủ nào.")
        return

    print("\n--- SÀN GIAO DỊCH TUYỂN THỦ ---")
    print(f"{'ID':<8} | {'Tên tuyển thủ':<15} | {'Giá trị thị trường':<18} | {'Fan Token':<10} | {'Điểm trận':<10} | {'Hệ số':<6} | Trạng thái đầu tư")
    print("-" * 110)
    
    for p in player_list:
        p_id = p.get("player_id", "N/A")
        name = p.get("name", "Unknown")
        market_value = f"{p.get('market_value', 0):,}"
        tokens = p.get("fan_tokens", 0)
        points = p.get("match_points", 0)
        multiplier = p.get("form_multiplier", 1.0)
        
        # Xác định trạng thái đầu tư theo quy định nghiệp vụ
        if tokens == 0:
            status = "Chưa có người đầu tư"
        elif tokens <= 1000:
            status = "Đang thu hút"
        else:
            status = "Tuyển thủ Hot"
            
        print(f"{p_id:<8} | {name:<15} | {market_value:<18} | {tokens:<10,} | {points:<10,} | {multiplier:<6.1f} | {status}")
        
    logging.info("User viewed the player market.")

def invest_tokens(player_list: list) -> None:
    """Chức năng 2: Đầu tư Fan Token"""
    print("\n--- ĐẦU TƯ FAN TOKEN ---")
    player_id = input("Nhập mã tuyển thủ: ").strip()
    idx = find_player_by_id(player_list, player_id)
    
    if idx == -1:
        print("\nKhông tìm thấy tuyển thủ!")
        logging.warning(f"Invest failed - Player {player_id.strip().upper()} not found")
        return

    target_player = player_list[idx]
    
    while True:
        try:
            token_input = input("Nhập số token muốn đầu tư: ").strip()
            amount = int(token_input)
            if amount <= 0:
                print("\nSố token phải là số nguyên dương. Vui lòng nhập lại.")
                continue
            break
        except ValueError:
            print("\nSố token phải là số nguyên dương. Vui lòng nhập lại.")
            logging.warning("Invalid token input while investing")

    target_player["fan_tokens"] = target_player.get("fan_tokens", 0) + amount
    print(f"\nThành công: Đã đầu tư {amount} token vào tuyển thủ {target_player['player_id']}.")
    print(f"Số Fan Token hiện tại của {target_player['name']}: {target_player['fan_tokens']:,}")
    logging.info(f"Invested {amount} tokens into {target_player['player_id']}")

def withdraw_tokens(player_list: list) -> None:
    """Chức năng 3: Rút vốn (Hoàn trả Token)"""
    print("\n--- RÚT VỐN FAN TOKEN ---")
    player_id = input("Nhập mã tuyển thủ: ").strip()
    idx = find_player_by_id(player_list, player_id)
    
    if idx == -1:
        print("\nKhông tìm thấy tuyển thủ!")
        logging.warning(f"Withdraw failed - Player {player_id.strip().upper()} not found")
        return

    target_player = player_list[idx]
    current_tokens = target_player.get("fan_tokens", 0)
    
    while True:
        try:
            token_input = input("Nhập số token muốn rút: ").strip()
            amount = int(token_input)
            if amount <= 0:
                print("\nSố token rút phải là số nguyên dương. Vui lòng nhập lại.")
                continue
            break
        except ValueError:
            print("\nSố token rút phải là số nguyên thực tế. Vui lòng nhập lại.")

    if amount > current_tokens:
        print("\nKhông thể rút. Số token muốn rút vượt quá số Fan Token hiện có.")
        print(f"Fan Token hiện có của {target_player['name']}: {current_tokens:,}")
        logging.warning("Withdraw failed - Amount exceeds current fan tokens")
        return

    # Sử dụng helper function tính tiền thực nhận sau phí 10%
    actual_received = calc_actual_withdrawal(amount)
    fee = amount - actual_received
    
    # Khấu trừ trực tiếp vào hệ thống dữ liệu tuyển thủ
    target_player["fan_tokens"] = current_tokens - amount
    
    print(f"\nThành công: Đã rút {amount} token khỏi tuyển thủ {target_player['player_id']}.")
    print(f"Phí giao dịch 10%: {fee:.1f} token")
    print(f"Số token thực nhận về ví: {actual_received:.1f} token")
    print(f"Fan Token còn lại của {target_player['name']}: {target_player['fan_tokens']:,}")
    logging.info(f"Withdrawn {amount} tokens from {target_player['player_id']}. Actual received: {actual_received}")

def update_form(player_list: list) -> None:
    """Chức năng 4: Biến động phong độ (Cập nhật hệ số)"""
    print("\n--- CẬP NHẬT HỆ SỐ PHONG ĐỘ ---")
    player_id = input("Nhập mã tuyển thủ: ").strip()
    idx = find_player_by_id(player_list, player_id)
    
    if idx == -1:
        print("\nKhông tìm thấy tuyển thủ!")
        return

    target_player = player_list[idx]
    
    while True:
        try:
            form_input = input("Nhập hệ số phong độ mới (0.5 - 2.5): ").strip()
            new_multiplier = float(form_input)
            if not (0.5 <= new_multiplier <= 2.5):
                print("\nHệ số phong độ chỉ được nằm trong khoảng 0.5 đến 2.5.")
                continue
            break
        except ValueError:
            print("\nHệ số phong độ phải là số thực. Vui lòng nhập lại.")

    target_player["form_multiplier"] = new_multiplier
    print(f"\nThành công: Đã cập nhật hệ số phong độ cho {target_player['name']}.")
    print(f"Hệ số mới: x{new_multiplier:.1f}")
    logging.info(f"Updated form multiplier for {target_player['player_id']} to {new_multiplier}")

def calculate_match_points(player_list: list) -> None:
    """Chức năng 5: Chấm điểm sau trận đấu"""
    print("\n--- CHẤM ĐIỂM SAU TRẬN ĐẤU ---")
    player_id = input("Nhập mã tuyển thủ: ").strip()
    idx = find_player_by_id(player_list, player_id)
    
    if idx == -1:
        print("\nKhông tìm thấy tuyển thủ!")
        return

    target_player = player_list[idx]
    
    while True:
        try:
            base_input = input("Nhập điểm gốc của trận đấu: ").strip()
            base_points = int(base_input)
            if base_points < 0:
                print("\nĐiểm gốc trận đấu phải lớn hơn hoặc bằng 0.")
                continue
            break
        except ValueError:
            print("\nĐiểm gốc phải là một số nguyên hợp lệ.")

    multiplier = target_player.get("form_multiplier", 1.0)
    earned_points = base_points * multiplier
    target_player["match_points"] = target_player.get("match_points", 0) + int(earned_points)
    
    print(f"\n>> Tuyển thủ {target_player['name']} nhận được {int(earned_points)} điểm (Hệ số x{multiplier:.1f}).")
    print(f"Tổng điểm: {target_player['match_points']:,}")
    logging.info(f"Added {earned_points} match points to {target_player['player_id']}")

def main() -> None:
    """Hàm khởi chạy điều khiển cấu trúc luồng menu chương trình"""
    while True:
        print("\n===== HỆ THỐNG RIKKEI ESPORTS FANTASY =====")
        print("1. Xem Sàn Giao Dịch Tuyển Thủ")
        print("2. Đầu tư Fan Token")
        print("3. Rút vốn (Hoàn trả Token)")
        print("4. Biến động phong độ (Cập nhật hệ số)")
        print("5. Chấm điểm sau trận đấu")
        print("6. Thoát hệ thống")
        print("==================================================")
        
        choice = input("Chọn chức năng (1-6): ").strip()
        
        # Sử dụng cấu trúc rẽ nhánh mặc định case theo yêu cầu
        match choice:
            case "1":
                display_market(players)
            case "2":
                invest_tokens(players)
            case "3":
                withdraw_tokens(players)
            case "4":
                update_form(players)
            case "5":
                calculate_match_points(players)
            case "6":
                print("\nĐóng hệ thống Rikkei Esports Fantasy.")
                logging.info("System closed.")
                break
            case _:
                print("\nLựa chọn không hợp lệ! Vui lòng chọn lại từ 1 đến 6.")

if __name__ == "__main__":
    main()