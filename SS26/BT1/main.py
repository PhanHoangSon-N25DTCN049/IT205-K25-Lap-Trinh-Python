from abc import ABC, abstractmethod

# Lớp trừu tượng: Kỹ năng tổng quát
class Skill(ABC):
    def __init__(self, skill_name, mana_cost):
        self.skill_name = skill_name
        self.mana_cost = mana_cost

    @abstractmethod
    def cast(self):
        """Phương thức trừu tượng bắt buộc các lớp con phải ghi đè"""
        pass


# Lớp con 1: Kỹ năng của Chiến binh
class WarriorSkill(Skill):
    def __init__(self, skill_name, mana_cost, physical_damage):
        super().__init__(skill_name, mana_cost)
        self.physical_damage = physical_damage

    def cast(self):
        # Ghi đè phương thức cast() xử lý logic của Chiến binh
        return f"[Warrior] Thi triển {self.skill_name} (Tốn {self.mana_cost} Mana) -> Gây {self.physical_damage} sát thương vật lý!"


# Lớp con 2: Kỹ năng của Pháp sư
class MageSkill(Skill):
    def __init__(self, skill_name, mana_cost, magic_damage):
        super().__init__(skill_name, mana_cost)
        self.magic_damage = magic_damage

    def cast(self):
        # SỬA LỖI: Ghi đè phương thức cast() bị bỏ quên để hiện thực hóa lớp trừu tượng
        return f"[Mage] Thi triển {self.skill_name} (Tốn {self.mana_cost} Mana) -> Gây {self.magic_damage} sát thương phép thuật!"


# --- HÀM VẬN HÀNH ĐA HÌNH (COMBAT PHASE) ---
def activate_combat_phase(skills_list):
    print("===== GIAI ĐOẠN GIAO TRANH BẮT ĐẦU =====")
    for skill in skills_list:
        # Cơ chế Đa hình tự động gọi đúng hàm cast() của từng lớp con tương ứng
        print(skill.cast())
    print("========================================")


# --- KỊCH BẢN CHẠY GAME ---
# Khởi tạo các kỹ năng hợp lệ (Lỗi TypeError đã được giải quyết)
slash = WarriorSkill("Kiếm Thần Khải Huyền", 20, 350)
fireball = MageSkill("Quả Cầu Lửa Hủy Diệt", 80, 600)

# Gom các đối tượng vào danh sách và kích hoạt giai đoạn chiến đấu
combat_skills = [slash, fireball]
activate_combat_phase(combat_skills)