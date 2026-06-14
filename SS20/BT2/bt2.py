
# 1. Lỗi IndexError tại 'r = p[2]': Do SofM chỉ có 2 phần tử ("SofM", 150), tương 
#    đương index 0 và 1. Khi code gọi p[2] (phần tử thứ 3) vượt quá phạm vi 
#    của Tuple nên hệ thống bị crash. Levi chạy được vì có đủ 3 phần tử.
# 2. Lỗi tại Optimus: Chương trình sẽ sập ở dòng `int(r)` do ép kiểu chuỗi "N/A" 
#    về số nguyên. Tên lỗi in ra màn hình Console sẽ là: ValueError.
# 3. Tác dụng lệnh print("Đang xử lý:", p): Giúp debug nhanh, biết chính xác 
#    chương trình đang chạy đến hồ sơ của tuyển thủ nào thì bị dừng lại.
# 4. Đổi tên biến theo Clean Code:
#    - ds -> player_records (Danh sách hồ sơ)
#    - p  -> record (Hồ sơ tuyển thủ)
#    - t  -> name (Tên tuyển thủ)
#    - m  -> matches (Số trận đã chơi)
#    - r  -> mmr (Điểm MMR)
#    - b  -> bonus (Tiền thưởng RP)

# Dữ liệu từ API: (Tên, Số trận, MMR)
data = [
    ("Levi", 120, 2500),      # Dữ liệu chuẩn
    ("SofM", 150),            # Lỗi API: Bị thiếu mất trường MMR
    ("Optimus", 100, "N/A")   # Lỗi dữ liệu: Điểm MMR bị ghi chữ "N/A"
]

def calculate_bonus(matches, mmr):
    """
    Hàm chuyên biệt để tính và trả về tiền thưởng RP dựa trên số trận và MMR.
    """
    return (matches * 10) + (int(mmr) * 0.5)

def process_player_bonuses(player_records):
    """
    Hàm duyệt danh sách và in tiền thưởng, có bẫy lỗi để tránh crash hệ thống.
    """
    print("--- BẢNG TÍNH THƯỞNG RP ---")
    
    for record in player_records:
        try:
            # Lấy thông tin cơ bản
            name = record[0]
            matches = record[1]
            mmr = record[2]  # Nếu thiếu phần tử, dòng này sẽ ném ra IndexError
            
            # Tính toán tiền thưởng
            bonus = calculate_bonus(matches, mmr)
            print(f"Tuyển thủ {name} nhận được {bonus} RP")
            
        except IndexError:
            # Lấy tên tuyển thủ từ phần tử đầu tiên nếu record vẫn có ít nhất 1 phần tử
            current_name = record[0] if len(record) > 0 else "Ẩn danh"
            print(f"[{current_name}]: Lỗi - Hồ sơ bị thiếu thông tin!")
            continue
            
        except ValueError:
            print(f"[{name}]: Lỗi - Dữ liệu MMR không hợp lệ!")
            continue

# Chạy hệ thống kiểm thử
process_player_bonuses(data)