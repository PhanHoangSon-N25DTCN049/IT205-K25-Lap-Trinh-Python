import itertools

teams_list = []
match_schedule = []

def nhap_danh_sach_doi():
    """Nhập danh sách đội tuyển từ người dùng, chuẩn hóa dữ liệu và lọc trùng."""
    print("\n--- NHẬP DANH SÁCH ---")
    raw_input = input("Nhập các đội (cách nhau bởi dấu phẩy): ")
    
    raw_teams = [team.strip().upper() for team in raw_input.split(',') if team.strip()]
    
    global teams_list
    teams_list = []
    for team in raw_teams:
        if team not in teams_list:
            teams_list.append(team)
            
    print(f"Đã ghi nhận {len(teams_list)} đội: {teams_list}")

def tao_lich_thi_dau(teams):
    """Tạo lịch thi đấu vòng tròn một lượt sử dụng itertools.combinations."""
    if len(teams) < 2:
        print("Lỗi: Cần tối thiểu 2 đội để tạo lịch thi đấu.")
        return []
        
    print("\n--- LỊCH THI ĐẤU VÒNG BẢNG ---")
    combinations = list(itertools.combinations(teams, 2))
    schedule = [f"{team1} vs {team2}" for team1, team2 in combinations]
    
    for idx, match in enumerate(schedule, 1):
        print(f"{idx}. {match}")
        
    print(f"Tổng số trận đấu: {len(schedule)} trận.")
    return schedule

def tao_ma_tran_dau(schedule):
    """Sinh mã trận đấu tự động từ lịch thi đấu sẵn có bằng F-String và padding."""
    if not schedule:
        print("Vui lòng tạo lịch thi đấu trước khi sinh mã ID.")
        return
        
    print("\n--- MÃ TRẬN ĐẤU (MATCH ID) ---")
    for idx, match in enumerate(schedule, 1):
        team1, team2 = match.split(' vs ')
        team1_code = f"{team1[0:3]:X<3}"
        team2_code = f"{team2[0:3]:X<3}"
        match_id = f"M{idx:02d}-{team1_code}-{team2_code}"
        print(f"Trận {idx} ({match}) -> ID: {match_id}")

def main():
    """Hàm điều khiển chính của hệ thống Esports Matchmaker."""
    global teams_list, match_schedule
    while True:
        print("\n============= ESPORTS MATCHMAKER =============")
        print("1. Nhập danh sách Đội tuyển")
        print("2. Tạo lịch thi đấu (Combinations)")
        print("3. Tạo mã trận đấu tự động (F-String & Cắt chuỗi)")
        print("4. Đóng hệ thống")
        print("==============================================")
        
        choice = input("Chọn chức năng (1-4): ")
        
        match choice:
            case '1':
                nhap_danh_sach_doi()
            case '2':
                match_schedule = tao_lich_thi_dau(teams_list)
            case '3':
                tao_ma_tran_dau(match_schedule)
            case '4':
                print("Đóng hệ thống. Tạm biệt!")
                break
            case _:
                print("Lựa chọn không hợp lệ, vui lòng thử lại.")

if __name__ == "__main__":
    main()