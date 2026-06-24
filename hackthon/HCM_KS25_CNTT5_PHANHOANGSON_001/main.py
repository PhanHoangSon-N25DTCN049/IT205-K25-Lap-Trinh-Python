class Player:
    def __init__(self, id:str, name:str, speed_score, technique_score, goad_score):
        self.id = id
        self.name = name
        self.speed_score = speed_score
        self.technique_score = technique_score
        self.goad_score = goad_score
        self.average_score = self.calculate_average()
        self.performance_style = self.classify_performance()
        
    def calculate_average(self) -> float:
        return float(self.speed_score * 0.3 + self.technique_score * 0.4 + self.goad_score * 0.3)
    
    def classify_performance(self):
        if self.average_score > 8.0:
            return "Ngôi sao"
        elif self.average_score >= 6.5:
            return "Tốt"
        elif self.average_score >= 5:
            return "Trung bình"
        else: 
            return "Dự bị yếu"
        
    
    
    
class PlayerManager(Player):
    def __init__(self):
        self.players = []
    
    def show_all(self, list_player):
        header = f"{"ID":<5} | {"Name":<15} | {"Tốc độ":<10} | {"Kĩ thuật":<10} | {"Ghi bàn":<10} | {"Điểm Phong độ":<13} | {"Phân loại":<10}"
        print("===================== Danh sách cầu thủ =====================")
        print("-"*len(header))
        print(header)
        print("-"*len(header))
        for player in list_player:
            print(f"{player.id:<5} | {player.name:<15} | {player.speed_score:<10} | {player.technique_score:<10} | {player.goad_score:<10} | {player.average_score:<13} | {player.performance_style:<10}")
        print("-"*len(header))
        print()
        
    def check_id(self, id):
        for idx,id_player in enumerate(self.players):
            if id == id_player:
                return idx
            return -1
    
            
    def add_player(self,id, name,speed_score,technique_score, goad_score):
        new_player = Player(id = id, name=name, speed_score=speed_score , technique_score=technique_score, goad_score=goad_score)
        self.players.append(new_player)
        print("Thêm cầu thủ thành công!")
        
    def update_player(self, idx):
        speed_score = float(input("Nhập Điểm tốc độ: "))
        technique_score = float(input("Nhập điểm kĩ thuật: "))
        goad_score = float(input("Nhập điểm ghi bàn: "))
        self.players[idx].speed_score = speed_score
        self.players[idx].technique_score = technique_score
        self.players[idx].goad_score = goad_score
        self.players[idx].average_score = Player.calculate_average(self.players[idx])
        self.players[idx].performance_style = Player.classify_performance(self.players[idx])
        print("Cập nhật cầu thủ thành công")
    
    def delete_player(self,idx):
        while True:
            choice = input("Bạn có chắc muốn xóa cầu thủ này không? (Y/N): ")
            match choice:
                case "Y" | "y":
                    del self.players[idx]
                    print("Đã xóa thành công")
                    break
                case "N" | "n":
                    print("Đã hủy thao tác")
                    break
                case _:
                    print("Nhập chưa đúng")
    def search_player(self, key):
        list_player = [player for player in self.players if key in player.name]
        self.show_all(list_player)


def validate_number (number):
    if number <= 0:
        return False
    return True

def main():
    Players = PlayerManager()
    while True:
        print("============ MENU ============")
        print("1. Hiển thị danh sách cầu thủ")
        print("2. Thêm cầu thủ mới")
        print("3. Cập nhật thông tin cầu thủ")
        print("4. Xóa cầu thủ")
        print("5. Tìm kiếm cầu thủ")
        print("6. Thoát")
        print("==============================")
        choice_main = input("Nhập lựa chọn của bạn: ")
        
        match choice_main:
            case "1":
                if Players.players == []:
                    print("Chưa có cầu thủ nào!")
                    continue
                Players.show_all(Players.players)
            case "2":
                id = input("Nhập Mã cầu thủ: ")
                while True:
                    name = input("Nhập tên cầu thủ: ")
                    if name.strip():
                        break
                    print("Tên không được bỏ trống")
                    
                speed_score = float(input("Nhập Điểm tốc độ: "))
                technique_score = float(input("Nhập điểm kĩ thuật: "))
                goad_score = float(input("Nhập điểm ghi bàn: "))
                Players.add_player(id, name, speed_score, technique_score, goad_score)
            case "3":
                if Players.players == []:
                    print("Chưa có cầu thủ nào!")
                    continue
                key = input("Nhập vào ID cầu thủ cần chỉnh sửa: ")
                idx = Players.check_id(key)
                if idx == -1:
                    print("Không tìm thấy thông tin cầu thủ")
                    continue
                Players.update_player(idx)
            case "4":
                if Players.players == []:
                    print("Chưa có cầu thủ nào!")
                    continue
                key = input("Nhập vào ID cầu thủ cần xóa: ")
                idx = Players.check_id(key)
                if idx == -1:
                    print("Không tìm thấy thông tin cầu thủ")
                    continue
                Players.delete_player(idx)
            case "5":
                if Players.players == []:
                    print("Chưa có cầu thủ nào!")
                    continue
                key = input("Nhập tên cầu thủ cần tìm: ")
                Players.search_player(key)
if __name__ == "__main__":
    main()