from abc import ABC, abstractmethod

class Champion(ABC):
    """
    Lớp trừu tượng đại diện cho một quân cờ (Champion) trong hệ thống game.
    """
    def __init__(self, champion_id, name, base_hp, base_atk):
        # Bẫy dữ liệu 2: Xử lý chỉ số âm hoặc bằng 0
        self.champion_id = champion_id
        self.name = name
        self.base_hp = base_hp if base_hp > 0 else 100
        self.base_atk = base_atk if base_atk > 0 else 100

    @abstractmethod
    def calculate_skill_damage(self):
        """Phương thức trừu tượng tính lượng sát thương kỹ năng."""
        pass

    def get_combat_power(self):
        """Tính điểm chiến lực tổng hợp của quân cờ."""
        return self.base_hp + (self.calculate_skill_damage() * 1.5)

    def __add__(self, other):
        """Nạp chồng toán tử + để cộng dồn điểm chiến lực."""
        if isinstance(other, Champion):
            return self.get_combat_power() + other.get_combat_power()
        elif isinstance(other, (int, float)):
            return self.get_combat_power() + other
        return NotImplemented

    def __radd__(self, other):
        """Hỗ trợ phép cộng đảo chiều khi số nguyên nằm bên trái (VD: 0 + Champion)."""
        return self.__add__(other)

    def __gt__(self, other):
        """Nạp chồng toán tử > để so sánh chiến lực giữa hai quân cờ."""
        if not isinstance(other, Champion):
            return NotImplemented
        return self.get_combat_power() > other.get_combat_power()


class Warrior(Champion):
    """Lớp cụ thể đại diện cho hệ tướng Chiến binh."""
    def __init__(self, champion_id, name, base_hp, base_atk, shield_bonus):
        super().__init__(champion_id, name, base_hp, base_atk)
        self.shield_bonus = shield_bonus if shield_bonus >= 0 else 0

    def calculate_skill_damage(self):
        """Ghi đè tính sát thương: Sát thương = ATK * 2 + Giáp cộng thêm"""
        return self.base_atk * 2 + self.shield_bonus


class Mage(Champion):
    """Lớp cụ thể đại diện cho hệ tướng Pháp sư."""
    def __init__(self, champion_id, name, base_hp, base_atk, ability_power):
        super().__init__(champion_id, name, base_hp, base_atk)
        self.ability_power = ability_power if ability_power > 0 else 1.0

    def calculate_skill_damage(self):
        """Ghi đè tính sát thương: Sát thương = ATK * Hệ số phép thuật"""
        return self.base_atk * self.ability_power


def main():
    # Khởi tạo bể tướng mặc định ban đầu
    champion_pool = {
        "WAR01": Warrior("WAR01", "Rikkei Knight", 1200, 300, 150),
        "WAR02": Warrior("WAR02", "Steel Guardian", 1500, 250, 200),
        "MAG01": Mage("MAG01", "Rikkei Wizard", 800, 500, 1.5)
    }

    while True:
        print("\n===== RIKKEI RPG - AUTO-BATTLER MANAGER =====")
        print("1. Hiển thị bể tướng hiện có")
        print("2. Thêm quân cờ mới")
        print("3. So sánh 2 quân cờ")
        print("4. Tính tổng chiến lực Đội Hình Ra Sân")
        print("5. Thoát chương trình")
        print("=============================================")
        
        choice = input("Chọn chức năng (1-5): ").strip()

        match choice:
            case "1":
                print("\n--- DANH SÁCH QUÂN CỜ TRONG BỂ TƯỚNG ---")
                print(f"{'Mã':<8} | {'Tên tướng':<18} | {'Hệ':<8} | {'HP':<5} | {'ATK':<5} | {'Chỉ số riêng':<15} | {'Chiến lực'}")
                print("-" * 80)
                for c in champion_pool.values():
                    he_toc = "Warrior" if isinstance(c, Warrior) else "Mage"
                    chi_so_rieng = f"Armor: {c.shield_bonus}" if isinstance(c, Warrior) else f"AP: {c.ability_power}"
                    print(f"{c.champion_id:<8} | {c.name:<18} | {he_toc:<8} | {c.base_hp:<5} | {c.base_atk:<5} | {chi_so_rieng:<15} | {c.get_combat_power():.0f}")
                print("-" * 80)

            case "2":
                print("\n--- TẠO TƯỚNG MỚI ---")
                print("1 - Hệ Warrior | 2 - Hệ Mage")
                type_choice = input("Chọn hệ tướng: ").strip()
                if type_choice not in ["1", "2"]:
                    print("Lựa chọn hệ tướng không hợp lệ.")
                    continue

                c_id = input("Nhập mã tướng: ").strip().upper()
                # Bẫy dữ liệu 4: Trùng mã tướng
                if c_id in champion_pool:
                    print(f"Lỗi: Mã tướng '{c_id}' đã tồn tại trong bể tướng!")
                    continue

                name = input("Nhập tên tướng: ").strip()
                
                try:
                    hp = int(input("Nhập HP: "))
                    atk = int(input("Nhập ATK: "))
                    
                    if type_choice == "1":
                        armor = int(input("Nhập Armor: "))
                        new_champion = Warrior(c_id, name, hp, atk, armor)
                        champion_pool[c_id] = new_champion
                        print(f"\nThêm tướng Warrior thành công!")
                    else:
                        ap = float(input("Nhập Ability Power (Hệ số phép): "))
                        new_champion = Mage(c_id, name, hp, atk, ap)
                        champion_pool[c_id] = new_champion
                        print(f"\nThêm tướng Mage thành công!")
                        
                    print(f"Mã: {new_champion.champion_id} | Tên: {new_champion.name} | Chiến lực: {new_champion.get_combat_power():.0f}")
                except ValueError:
                    print("Lỗi: Nhập sai định dạng dữ liệu số! Vui lòng thao tác lại.")

            case "3":
                print("\n--- SO SÁNH SỨC MẠNH 2 QUÂN CỜ ---")
                id1 = input("Nhập mã tướng thứ nhất: ").strip().upper()
                id2 = input("Nhập mã tướng thứ hai: ").strip().upper()

                c1 = champion_pool.get(id1)
                c2 = champion_pool.get(id2)

                # Bẫy dữ liệu 3: Mã tướng không tồn tại
                if not c1:
                    print(f"Mã tướng {id1} không hợp lệ, bỏ qua!")
                    continue
                if not c2:
                    print(f"Mã tướng {id2} không hợp lệ, bỏ qua!")
                    continue

                print("\nThông tin so sánh:")
                print(f"{c1.champion_id} - {c1.name} | Hệ: {'Warrior' if isinstance(c1, Warrior) else 'Mage'} | Chiến lực: {c1.get_combat_power():.0f}")
                print(f"{c2.champion_id} - {c2.name} | Hệ: {'Warrior' if isinstance(c2, Warrior) else 'Mage'} | Chiến lực: {c2.get_combat_power():.0f}")
                
                # Áp dụng nạp chồng toán tử >
                if c1 > c2:
                    print(f"Kết quả: {c1.champion_id} - {c1.name} mạnh hơn {c2.champion_id} - {c2.name}.")
                elif c2 > c1:
                    print(f"Kết quả: {c2.champion_id} - {c2.name} mạnh hơn {c1.champion_id} - {c1.name}.")
                else:
                    print("Kết quả: Hai quân cờ có chiến lực ngang nhau.")

            case "4":
                print("\n--- TÍNH TỔNG CHIẾN LỰC ĐỘI HÌNH RA SÂN ---")
                raw_input = input("Nhập danh sách mã tướng, cách nhau bằng dấu phẩy: ")
                input_ids = [i.strip().upper() for i in raw_input.split(",") if i.strip()]

                team_lineup = []
                for c_id in input_ids:
                    champion = champion_pool.get(c_id)
                    if champion:
                        team_lineup.append(champion)
                    else:
                        # Bẫy dữ liệu 3: Không tồn tại thì bỏ qua không crash
                        print(f"Mã tướng [{c_id}] không hợp lệ, bỏ qua!")

                if not team_lineup:
                    print("Không có tướng hợp lệ nào trong đội hình vừa chọn.")
                    continue

                print("\nDanh sách đội hình:")
                for index, c in enumerate(team_lineup, start=1):
                    print(f"{index}. {c.champion_id} - {c.name} | Chiến lực: {c.get_combat_power():.0f}")

                # Áp dụng nạp chồng toán tử + để cộng dồn điểm chiến lực toàn đội
                total_power = sum(team_lineup)
                print(f"Tổng chiến lực đội hình: {total_power:.0f}")

            case "5":
                print("Cảm ơn bạn đã sử dụng Rikkei RPG - Auto-Battler Manager!")
                break

            case _:
                print("Chức năng lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 5.")

if __name__ == "__main__":
    main()