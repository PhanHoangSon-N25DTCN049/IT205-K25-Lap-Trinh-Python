from abc import ABC, abstractmethod
class BaseCharacter:
    def __init__(self, hp, strength ):
        self.__base_hp = hp
        self.strength  = strength  
        
    @property
    def base_hp(self):
        return self.__base_hp
    
    @abstractmethod
    def attack_enemy(self):
        return 150.0
        
    def __add__(self, other: "BaseCharacter"):
        return self.base_hp + other.base_hp
    
    
class MagicalStance(BaseCharacter):
    def __init__(self, hp, strength ):
        super().__init__(hp, strength )
    
    def attack_enemy(self):
        return 150.0

class Warrior(BaseCharacter):
    def __init__(self, hp, strength):
        super().__init__(hp, strength)

    def attack_enemy(self):
        return self.strength * 2.5
    
class Spellblade(Warrior, MagicalStance):
    def __init__(self, hp, strength):
        super().__init__(hp, strength)
        
    def attack_enemy(self):
        return self.strength * 2.5 + 150.0
    
    
class VolcanoZone:
    def activate_buff(character):
        print("[Volcano Zone Effect]: Sức nóng dung nham kích hoạt! gia tăng +20% sát thương cho Warrior") 
    
def apply_battleground_effect(environment, character):
    print("[Duck Typing]: Xác thực môi trường trận đấu thành công")
    environment.activate_buff(character)

def main():
    current_hero = None
    while True:
        choice = input("""
==== RPG GAME CORE MENU ====
1. Khởi tạo ma kiếm sĩ spellblade & xem cấu trúc MRO
2. Ra lệnh tấn công & kích hoạt chiến trường
Chọn chức năng (1-2): """);
        match choice:
            case "1":
                print("---- Khởi tạo ma kiếm sĩ ---")
                while True: 
                    try:   
                        hp = int(input("Nhập lượng máu cơ bản: "))
                        if hp > 0:
                            break
                    except ValueError:
                        print("Lượng máu không được nhỏ hơn hoặc bằng 0")
                while True:    
                    try:   
                        strength = int(input("Chỉ số sức mạnh: "))
                        if strength > 0:
                            break
                    except ValueError:
                        print("sức mạnh không được nhỏ hơn hoặc bằng 0")   
                current_hero = Spellblade(hp, strength)
                print("Thành công: Khởi tạo nhân vật Spellblade thành công!")
                list_cls = [cls.__name__ for cls in type(current_hero).__mro__]
                print(f"[MRO architecture]: {" -> ".join(list_cls)}")
                print(f"[Overloading __add__]: Tổng HP tích lũy khi gộp đội hình: {current_hero + current_hero}")
                
            case "2":
                if current_hero == None:
                    print("Chưa có nhân vật nào được tạo");
                    continue
                print("--- THI THIẾT KẾ GIAO TRANH & DUCK TYPING ---")
                print(f"[Đa hình]: Spellblade vung kiếm ma thuật gây tổng sát thương: {current_hero.attack_enemy()} DMG")
                apply_battleground_effect(VolcanoZone, current_hero)
            case _:
                print("Lỗi lựa chọn vui lòng chọn lại!")
                
if __name__ == "__main__":
    main()