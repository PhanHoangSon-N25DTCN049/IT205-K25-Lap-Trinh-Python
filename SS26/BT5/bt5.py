from abc import ABC, abstractmethod

# ----------------- KIẾN TRÚC HỆ THỐNG CLASS -----------------

class Companion(ABC):
    """Lớp trừu tượng gốc quản lý tất cả Bạn đồng hành."""
    def __init__(self, name, level=1, **kwargs):
        super().__init__(**kwargs)  # Đảm bảo luồng MRO chuyển tiếp an toàn
        self.name = name
        self.level = level

    @abstractmethod
    def unleash_skill(self):
        """Phương thức trừu tượng buộc các lớp con bắt buộc phải ghi đè."""
        pass

    def __add__(self, other):
        """Nạp chồng toán tử + để xử lý cơ chế Lai tạo sinh vật."""
        # BẪY 2: Ngăn chặn dị giáo lai tạo (khác loài hoặc cộng với số)
        if type(self) != type(other):
            raise TypeError("Chỉ có thể lai tạo 2 sinh vật cùng loài!")
        
        new_name = f"{self.name} {other.name}"
        new_level = self.level + 1
        
        # Kiểm tra kiểu lớp thực tế để trả về đối tượng tương ứng với đầy đủ chỉ số cộng dồn
        if isinstance(self, Dragon):
            return Dragon(
                name=new_name,
                level=new_level,
                bonus_atk=self.bonus_atk + other.bonus_atk,
                bonus_speed=self.bonus_speed + other.bonus_speed
            )
        elif isinstance(self, Pet):
            return Pet(
                name=new_name,
                level=new_level,
                bonus_atk=self.bonus_atk + other.bonus_atk
            )
        elif isinstance(self, Mount):
            return Mount(
                name=new_name,
                level=new_level,
                bonus_speed=self.bonus_speed + other.bonus_speed
            )
        return NotImplemented


class Pet(Companion):
    """Lớp Thú cưng - Hỗ trợ chiến đấu."""
    def __init__(self, name, bonus_atk, level=1, **kwargs):
        # BẪY 3: Đẩy các tham số còn thừa lên lớp kế tiếp trong chuỗi MRO
        super().__init__(name=name, level=level, **kwargs)
        self.bonus_atk = bonus_atk

    def unleash_skill(self):
        return f"Tấn công kẻ thù, gây {self.bonus_atk} sát thương!"


class Mount(Companion):
    """Lớp Thú cưỡi - Hỗ trợ di chuyển."""
    def __init__(self, name, bonus_speed, level=1, **kwargs):
        # BẪY 3: Đẩy các tham số còn thừa lên lớp kế tiếp trong chuỗi MRO
        super().__init__(name=name, level=level, **kwargs)
        self.bonus_speed = bonus_speed

    def unleash_skill(self):
        return f"Tăng tốc độ di chuyển thêm {self.bonus_speed} điểm!"


class Dragon(Pet, Mount):
    """Lớp Rồng Thần - Đa kế thừa hoàn chỉnh áp dụng giải thuật MRO."""
    def __init__(self, name, bonus_atk, bonus_speed, level=1):
        # BẪY 3: Sử dụng kwargs để phân phối chỉ số chính xác cho cả Pet và Mount
        super().__init__(
            name=name,
            level=level,
            bonus_atk=bonus_atk,
            bonus_speed=bonus_speed
        )

    def unleash_skill(self):
        """Kích hoạt đồng thời cả hai kỹ năng của lớp cha."""
        # Gọi trực tiếp qua tên lớp để lấy chuỗi hành động cụ thể rõ ràng
        skill_pet = Pet.unleash_skill(self)
        skill_mount = Mount.unleash_skill(self)
        return f"   - {skill_pet}\n   - {skill_mount}"


# ----------------- KỊCH BẢN MÔ PHỎNG & CHỐNG BẪY DỮ LIỆU -----------------

if __name__ == "__main__":
    print("=== KIỂM TRA BẪY 1: Bảo vệ kiến trúc (ABC Trap) ===")
    try:
        error_companion = Companion("Lỗi Hệ Thống")
    except TypeError as e:
        print(f"Thành công! Hệ thống đã ngăn chặn khởi tạo trực tiếp: {e}\n")

    print("=== KHỞI TẠO DỮ LIỆU BAN ĐẦU ===")
    p1 = Pet("Sói Trắng", bonus_atk=50)
    p2 = Pet("Sói Đen", bonus_atk=60)
    m1 = Mount("Hắc Mã", bonus_speed=20)
    
    # BẪY 3 TEST: Khởi tạo Rồng kiểm tra tính toàn vẹn chỉ số
    d1 = Dragon("Rồng Lửa", bonus_atk=500, bonus_speed=200)
    print(f"Khởi tạo {d1.name} -> Atk: {d1.bonus_atk}, Speed: {d1.bonus_speed} (Không bị mất chỉ số!)")

    print("\n=== KIỂM TRA TÍNH NĂNG LAI TẠO (Operator Overloading) ===")
    p3 = p1 + p2
    print(f">> Lai tạo thành công! Nhận được: {p3.name} (Cấp {p3.level}, Atk: +{p3.bonus_atk})\n")

    print("=== KIỂM TRA BẪY 2: Dị giáo lai tạo (Operator Trap) ===")
    try:
        print("Thử thách lai tạo: Pet + Mount...")
        failed_breed_1 = p1 + m1
    except TypeError as e:
        print(f"Bẫy lỗi thành công: {e}")

    try:
        print("Thử thách lai tạo: Pet + Số nguyên...")
        failed_breed_2 = p1 + 100
    except TypeError as e:
        print(f"Bẫy lỗi thành công: {e}\n")

    # Tạo mảng danh sách quản lý đội hình ra sân
    active_companions = [p3, m1, d1]

    print("=== CHỨC NĂNG 1: XEM ĐỘI HÌNH SINH VẬT ===")
    for idx, companion in enumerate(active_companions, start=1):
        if isinstance(companion, Dragon):
            info = f"Atk: +{companion.bonus_atk} | Speed: +{companion.bonus_speed}"
            tag = "[Dragon]"
        elif isinstance(companion, Pet):
            info = f"Atk: +{companion.bonus_atk}"
            tag = "[Pet]"
        else:
            info = f"Speed: +{companion.bonus_speed}"
            tag = "[Mount]"
            
        print(f"{idx}. {tag} {companion.name:<18} | Cấp: {companion.level} | {info}")

    print("\n=== CHỨC NĂNG 5: XUẤT CHIẾN (Tính Đa Hình) ===")
    for companion in active_companions:
        if isinstance(companion, Dragon):
            print(f">> {companion.name} thị uy: \n{companion.unleash_skill()}")
        elif isinstance(companion, Pet):
            print(f">> {companion.name} gầm gừ: {companion.unleash_skill()}")
        else:
            print(f">> {companion.name} hí vang: {companion.unleash_skill()}")