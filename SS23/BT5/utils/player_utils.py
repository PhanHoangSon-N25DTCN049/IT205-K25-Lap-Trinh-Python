def find_player(records, player_id):
    """
    Tìm kiếm và trả về vị trí index của người chơi trong danh sách.
    Hỗ trợ bẫy dữ liệu chuẩn hóa mã (Bẫy 1).
    """
    clean_id = player_id.strip().upper()
    for index, player in enumerate(records):
        if player["player_id"] == clean_id:
            return index
    return -1