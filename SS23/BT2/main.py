import math
import os
from datetime import datetime

"""
1. Tác hại của việc sử dụng 'from datetime import *':
   - Gây ô nhiễm không gian tên (Namespace Pollution): Nạp rất nhiều class không cần thiết trực tiếp vào global namespace.
   - Xung đột tên (Name Collision): Nếu hệ thống đang có biến toàn cục 'time = 120', lệnh import này sẽ được thực thi 
     và ghi đè hoàn toàn biến cũ bằng class 'datetime.time'. Khi chương trình gọi lại biến 'time' để tính toán, 
     Python sẽ báo lỗi 'TypeError' vì không thể thực hiện phép toán trên một class, gây sập hệ thống.

2. Hàm tối ưu hơn os.mkdir():
   - Đó là hàm 'os.makedirs(path, exist_ok=True)'.
   - Ưu điểm: Cho phép tạo các thư mục lồng nhau dạng cây (ví dụ: media_vault/2026/video). Tham số 'exist_ok=True' 
     giúp bỏ qua lỗi 'FileExistsError' một cách an toàn nếu thư mục đã tồn tại trước đó, không cần check if-else thủ công.

3. Sơ đồ cấu trúc cây thư mục (Folder Tree) nếu tách file theo Package:
   rikkei_media/
   ├── storage/
   │   ├── __init__.py
   │   ├── disk_manager.py
   │   └── io_helper.py
   ├── analytics/
   │   ├── __init__.py
   │   └── time_validator.py
   └── main.py
"""


# --- Mô phỏng storage/disk_manager.py ---
def calculate_disk_blocks(size_bytes, block_size=4096):
    """
    Tính chính xác số block bộ nhớ tiêu tốn bằng hàm làm tròn lên math.ceil.
    """
    if size_bytes <= 0:
        return 0
    return math.ceil(size_bytes / block_size)


# --- Mô phỏng storage/io_helper.py ---
def safe_create_dir(path):
    """
    Khởi tạo thư mục lưu trữ một cách an toàn, tự động kiểm tra nếu thư mục tồn tại thì bỏ qua.
    """
    os.makedirs(path, exist_ok=True)


# --- Mô phỏng analytics/time_validator.py ---
def parse_and_inspect_date(date_str):
    """
    Bẫy lỗi dữ liệu ngày tháng không hợp lệ (như ngày 31/06) bằng try-except, 
    trả về thông báo lỗi và không làm sập chương trình.
    """
    try:
        valid_date = datetime.strptime(date_str, "%Y-%m-%d")
        return valid_date
    except ValueError as e:
        return str(e)



raw_files = [
    {"filename": "pod_ep1.mp3", "size_bytes": 4500, "duration_sec": 180, "upload_at": "2026-06-10"},
    {"filename": "movie_trailer.mp4", "size_bytes": 105000, "duration_sec": 145, "upload_at": "2026-06-31"},
    {"filename": "clip_short.mp4", "size_bytes": 8200, "duration_sec": 15, "upload_at": "2026-05-15"}
]

def main():
    print("======== HỆ THỐNG QUẢN LÝ LƯU TRỮ RIKKEI MEDIA =======")
    print("[SYSTEM] Kiểm tra hạ tầng lưu trữ... Hoàn tất.")
    print("-" * 75)

    success_count = 0
    total_files = len(raw_files)

    for file_info in raw_files:
        filename = file_info["filename"]
        size_bytes = file_info["size_bytes"]
        upload_at = file_info["upload_at"]

        print(f"[TỆP TIN: {filename}]")

        date_result = parse_and_inspect_date(upload_at)

        if isinstance(date_result, str):
            print(f" + Trạng thái phân loại: 🔴 THẤT BẠI (Lỗi: Định dạng ngày upload '{upload_at}' không tồn tại)\n")
            continue

        blocks = calculate_disk_blocks(size_bytes)

        if filename.lower().endswith(('.mp4', '.mkv', '.avi')):
            category = "video"
        elif filename.lower().endswith(('.mp3', '.wav', '.aac')):
            category = "audio"
        else:
            category = "others"

        target_dir = f"media_vault/{category}"
        safe_create_dir(target_dir)

        print(f" + Dung lượng thực tế: {size_bytes:,} Bytes")
        print(f" + Số khối phân vùng (4KB Block): {blocks} Blocks")
        print(f" + Trạng thái phân loại: 🟢 HỢP LỆ (Lưu trữ vào thư mục '{category}')\n")
        
        success_count += 1

    print("========================================================")
    print(f"TIẾN ĐỘ QUÉT: Hoàn thành xử lý {success_count}/{total_files} tệp tin thành công. Hệ thống ổn định.")

if __name__ == "__main__":
    main()