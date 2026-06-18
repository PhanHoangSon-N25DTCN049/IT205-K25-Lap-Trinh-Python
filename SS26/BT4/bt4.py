from abc import ABC, abstractmethod

# ----------------- ĐỊNH NGHĨA CÁC LỚP (ARCHITECTURE CLASS) -----------------

class Equipment(ABC):
    """Lớp trừu tượng gốc quản lý toàn bộ trang bị."""
    
    @abstractmethod
    def calculate_total_damage(self):
        """Bắt buộc tất cả các trang bị con phải định nghĩa công thức sát thương."""
        pass


class Weapon(Equipment):
    """Lớp vũ khí vật lý cơ bản."""
    def __init__(self, name, base_damage, upgrade_level=0):
        # Bẫy dữ liệu 2: Xử lý giá trị đầu vào hợp lệ
        self.name = name.title()
        self.base_damage = base_damage if base_damage > 0 else 100
        self.upgrade_level = upgrade_level if upgrade_level >= 0 else 0

    def calculate_total_damage(self):
        """Sát thương = Sát thương gốc + (Cấp cường hóa * 10)"""
        return self.base_damage + (self.upgrade_level * 10)

    def __gt__(self, other):
        """Nạp chồng toán tử > để thẩm định vũ khí (Bẫy dữ liệu 2)."""
        if not isinstance(other, Equipment):
            print("Chỉ có thể dung hợp/so sánh giữa các trang bị!")
            return NotImplemented
        return self.calculate_total_damage() > other.calculate_total_damage()

    def __add__(self, other):
        """Nạp chồng toán tử + để dung hợp hai vũ khí (Bẫy dữ liệu 2)."""
        if not isinstance(other, Equipment):
            print("Chỉ có thể dung hợp/so sánh giữa các trang bị!")
            return NotImplemented
            
        # Tính toán thông số cho vũ khí ghép mới
        new_name = f"Fusion({self.name} + {other.name})"
        new_base_damage = self.base_damage + other.base_damage
        new_upgrade_level = self.upgrade_level + other.upgrade_level
        
        # Đề bài yêu cầu tạo ra đối tượng Weapon mới, không phải MagicSword
        return Weapon(new_name, new_base_damage, new_upgrade_level)


class MagicMixin:
    """Lớp bổ trợ cung cấp thuộc tính phép thuật."""
    def __init__(self, magic_power):
        # Bẫy dữ liệu 2: Xử lý chỉ số ma thuật
        self.magic_power = magic_power if magic_power > 0 else 0

    def cast_glow(self):
        return f"✨ Vũ khí '{self.magic_power}' đang tỏa ra vầng hào quang ma mị!"


class MagicSword(Weapon, MagicMixin):
    """Lớp Kiếm Ma Thuật áp dụng đa kế thừa (Bẫy dữ liệu 3)."""
    def __init__(self, name, base_damage, upgrade_level, magic_power):
        # Gọi khởi tạo theo đúng cấu trúc phân giải MRO
        Weapon.__init__(self, name, base_damage, upgrade_level)
        MagicMixin.__init__(self, magic_power)

    def calculate_total_damage(self):
        """Sát thương tổng = Sát thương vật lý + Sức mạnh phép thuật"""
        return Weapon.calculate_total_damage(self) + self.magic_power


# ----------------- CHƯƠNG TRÌNH ĐIỀU HƯỚNG MENU -----------------

def main():
    inventory = []

    while True:
        print("\n===== LÒ RÈN VŨ KHÍ RIKKEI STUDIOS ===================")
        print("1. Xem kho vũ khí & Sát thương tổng")
        print("2. Rèn Vũ khí Vật lý (Tạo Weapon)")
        print("3. Rèn Kiếm Ma Thuật (Tạo MagicSword)")
        print("4. Thẩm định vũ khí (So sánh lớn hơn)")
        print("5. Dung hợp vũ khí (Cộng dồn cấp độ)")
        print("6. Thoát game")
        print("======================================================")

        choice = input("Chọn chức năng (1-6): ").strip()

        match choice:
            case "1":
                print("\n--- KHO VŨ KHÍ CỦA NGƯỜI CHƠI ---")
                if not inventory:
                    print("Kho vũ khí hiện đang trống.")
                    print("Vui lòng rèn vũ khí bằng Chức năng 2 hoặc Chức năng 3.")
                    continue

                print(f"{'STT':<5} | {'Tên vũ khí':<30} | {'Loại':<12} | {'Cấp':<5} | {'Sát thương tổng'}")
                print("-" * 75)
                for idx, item in enumerate(inventory, start=1):
                    item_type = "MagicSword" if isinstance(item, MagicSword) else "Weapon"
                    print(f"{idx:<5} | {item.name:<30} | {item_type:<12} | {item.upgrade_level:<5} | {item.calculate_total_damage()}")
                print("-" * 75)

            case "2":
                print("\n--- RÈN VŨ KHÍ VẬT LÝ ---")
                name = input("Nhập tên vũ khí: ").strip()
                if not name:
                    print("Tên vũ khí không được để trống!")
                    continue
                try:
                    base_dmg = int(input("Nhập sát thương gốc: "))
                    if base_dmg <= 0:
                        print("Giá trị phải lớn hơn 0!")
                        continue
                    
                    upgrade_lvl = int(input("Nhập cấp cường hóa: "))
                    if upgrade_lvl < 0:
                        print("Giá trị phải lớn hơn hoặc bằng 0!")
                        continue

                    # Tạo đối tượng Weapon và đưa vào túi đồ
                    new_weapon = Weapon(name, base_dmg, upgrade_lvl)
                    inventory.append(new_weapon)

                    print("\n>> Rèn vũ khí vật lý thành công!")
                    print(f"Tên vũ khí: {new_weapon.name}")
                    print("Loại: Weapon")
                    print(f"Cấp cường hóa: {new_weapon.upgrade_level}")
                    print(f"Sát thương tổng: {new_weapon.calculate_total_damage()}")
                except ValueError:
                    print("Lỗi: Vui lòng nhập dữ liệu định dạng số nguyên!")

            case "3":
                print("\n--- RÈN KIẾM MA THUẬT ---")
                name = input("Nhập tên kiếm ma thuật: ").strip()
                if not name:
                    print("Tên vũ khí không được để trống!")
                    continue
                try:
                    base_dmg = int(input("Nhập sát thương gốc: "))
                    if base_dmg <= 0:
                        print("Giá trị phải lớn hơn 0!")
                        continue

                    upgrade_lvl = int(input("Nhập cấp cường hóa: "))
                    if upgrade_lvl < 0:
                        print("Giá trị phải lớn hơn hoặc bằng 0!")
                        continue

                    magic_pwr = int(input("Nhập sức mạnh phép thuật: "))
                    if magic_pwr <= 0:
                        print("Giá trị phải lớn hơn 0!")
                        continue

                    # Tạo đối tượng MagicSword và đưa vào túi đồ
                    new_magic_sword = MagicSword(name, base_dmg, upgrade_lvl, magic_pwr)
                    inventory.append(new_magic_sword)

                    print("\n>> Rèn kiếm ma thuật thành công!")
                    print(f"Tên vũ khí: {new_magic_sword.name}")
                    print("Loại: MagicSword")
                    print(f"Cấp cường hóa: {new_magic_sword.upgrade_level}")
                    print(f"Sát thương gốc: {new_magic_sword.base_damage}")
                    print(f"Sức mạnh phép thuật: {new_magic_sword.magic_power}")
                    print(f"Sát thương tổng: {new_magic_sword.calculate_total_damage()}")
                    print(new_magic_sword.cast_glow())
                except ValueError:
                    print("Lỗi: Vui lòng nhập dữ liệu định dạng số nguyên!")

            case "4":
                print("\n--- THẨM ĐỊNH VŨ KHÍ ---")
                if len(inventory) < 2:
                    print("Cần ít nhất 2 vũ khí trong kho để thẩm định!")
                    continue

                w1 = inventory[0]
                w2 = inventory[1]

                type_w1 = "MagicSword" if isinstance(w1, MagicSword) else "Weapon"
                type_w2 = "MagicSword" if isinstance(w2, MagicSword) else "Weapon"

                print("Vũ khí thứ nhất:")
                print(f"{w1.name} | Loại: {type_w1} | Sát thương: {w1.calculate_total_damage()}\n")
                print("Vũ khí thứ hai:")
                print(f"{w2.name} | Loại: {type_w2} | Sát thương: {w2.calculate_total_damage()}\n")

                # Sử dụng toán tử so sánh đã nạp chồng >
                if w1 > w2:
                    print(f"Kết quả: {w1.name} mạnh hơn {w2.name}.")
                elif w2 > w1:
                    print(f"Kết quả: {w2.name} mạnh hơn {w1.name}.")
                else:
                    print("Kết quả: Hai vũ khí có sức mạnh ngang nhau.")

            case "5":
                print("\n--- DUNG HỢP VŨ KHÍ ---")
                if len(inventory) < 2:
                    print("Cần ít nhất 2 vũ khí trong kho để dung hợp!")
                    continue

                print("Đang dung hợp 2 vũ khí đầu tiên trong kho...\n")
                w1 = inventory[0]
                w2 = inventory[1]

                print(f"Vũ khí 1: {w1.name} | Cấp: {w1.upgrade_level} | Sát thương: {w1.calculate_total_damage()}")
                print(f"Vũ khí 2: {w2.name} | Cấp: {w2.upgrade_level} | Sát thương: {w2.calculate_total_damage()}")

                # Thực hiện phép cộng nạp chồng toán tử +
                new_fusion_weapon = w1 + w2

                # Xóa 2 vũ khí cũ khỏi đầu mảng danh sách kho đồ
                del inventory[0]
                del inventory[0] # Phần tử thứ 2 đôn lên làm phần tử thứ 0

                # Thêm món đồ mới rèn được vào kho đồ người chơi
                inventory.append(new_fusion_weapon)

                print("\n>> Dung hợp vũ khí thành công!")
                print(f"Đã xóa khỏi kho: {w1.name}")
                print(f"Đã xóa khỏi kho: {w2.name}\n")
                print(f"Vũ khí mới: {new_fusion_weapon.name}")
                print("Loại: Weapon")
                print(f"Cấp cường hóa: {new_fusion_weapon.upgrade_level}")
                print(f"Sát thương tổng: {new_fusion_weapon.calculate_total_damage()}")

            case "6":
                print("Thoát Lò Rèn. Hẹn gặp lại Anh hùng!")
                break

            case _:
                print("Chức năng lựa chọn không hợp lệ. Vui lòng chọn lại menu từ 1 đến 6.")

if __name__ == "__main__":
    main()