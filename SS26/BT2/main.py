from abc import ABC, abstractmethod

# Lớp cha: Khuôn mẫu Tướng sử dụng thư viện ABC chuẩn chỉnh
class Hero(ABC):
    
    @abstractmethod
    def use_ultimate(self):
        """Phương thức trừu tượng bắt buộc các hệ tướng con phải ghi đè"""
        pass

# Lớp con 1: Pháp Sư (Code đúng)
class Mage(Hero):
    def use_ultimate(self):
        print("🔥 Pháp Sư tung chiêu: MƯA SAO BĂNG!")

# Lớp con 2: Sát Thủ (Đã sửa lỗi thiết kế)
class Assassin(Hero):
    # SỬA LỖI: Đổi tên từ stealth_kill sang use_ultimate để ghi đè đúng khuôn mẫu
    def use_ultimate(self):
        print("🗡️ Sát Thủ tung chiêu: ÁM SÁT TỪ PHÍA SAU!")


# --- KỊCH BẢN VẬN HÀNH SAU KHI FIX BUG ---
print("--- LOADING TRẬN ĐẤU ---")
# Nếu lớp Assassin chưa ghi đè use_ultimate, dòng dưới đây sẽ văng lỗi crash ngay lập tức (Fail Fast)
team_heroes = [Mage(), Assassin()] 
print("Tải trận đấu thành công! Các tướng đã sẵn sàng...")

print("\n--- GIAO TRANH TỔNG BẮT ĐẦU ---")
# Vòng lặp Đa hình vận hành trơn tru và an toàn
for hero in team_heroes:
    hero.use_ultimate()