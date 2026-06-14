
# 1. Lỗi ZeroDivisionError: Do trong toán học không thể chia cho 0. Khi chạy đến 
#    ShowMaker có Deaths = "0", phép toán (15 + 10) / 0 kích hoạt ngoại lệ này.
#    Vì code cũ không bẫy lỗi bằng try...except nên chương trình bị sập luôn, 
#    khiến tuyển thủ phía sau không được xử lý.
# 2. Lỗi xảy ra với Chovy nếu xóa ShowMaker: Sẽ báo lỗi ValueError. Vì mạng chết
#    của Chovy bị điền nhầm thành chữ "ba", hàm int("ba") không thể chuyển đổi 
#    chuỗi ký tự chữ thành số nguyên được.
# 3. Đổi tên biến theo Clean Code (Self-documenting):
#    - ds -> player_list (Danh sách tuyển thủ)
#    - x  -> player (Vòng lặp duyệt từng tuyển thủ)
#    - n  -> name (Tên tuyển thủ)
#    - k  -> kills (Số mạng hạ gục)
#    - d  -> deaths (Số mạng nằm xuống)
#    - a  -> assists (Số mạng hỗ trợ)
# 4. Lợi ích tách hàm calculate_kda (Nguyên tắc DRY): giúp tái sử dụng code ở nơi 
#    khác mà không cần viết lại công thức, dễ bảo trì khi ban tổ chức đổi công thức 
#    tính, giúp cấu trúc hàm chính sạch sẽ và rõ ràng hơn.

tournament_data = [
    ("Faker", "10", "2", "8"),
    ("ShowMaker", "15", "0", "10"),
    ("Chovy", "12", "ba", "5"),
    ("Viper", "8", "1", "7")
]

def calculate_kda(kills, deaths, assists):
    """
    Hàm chuyên biệt để ép kiểu dữ liệu và tính toán chỉ số KDA.
    """
    int_kills = int(kills)
    int_deaths = int(deaths)
    int_assists = int(assists)
    
    if int_deaths == 0:
        raise ZeroDivisionError
        
    return (int_kills + int_assists) / int_deaths

def process_tournament_stats(player_list):
    """
    Hàm duyệt danh sách tuyển thủ và in kết quả ra màn hình.
    Sử dụng try...except để hệ thống không bị sập giữa chừng.
    """
    print("--- BẢNG XẾP HẠNG KDA ---")
    
    for player in player_list:
        name = player[0]
        kills = player[1]
        deaths = player[2]
        assists = player[3]
        
        try:
            # Gọi hàm tính KDA
            kda = calculate_kda(kills, deaths, assists)
            print(f"Tuyển thủ {name} có chỉ số KDA là: {kda:.1f}")
            
        except ZeroDivisionError:
            print(f"[{name}]: KDA Hoàn hảo (Perfect Game)!")
            continue
            
        except ValueError:
            print(f"[{name}]: Lỗi dữ liệu không hợp lệ!")
            continue
            
    print("--- HOÀN TẤT ---")


process_tournament_stats(tournament_data)