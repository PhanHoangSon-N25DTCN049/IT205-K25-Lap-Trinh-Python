import os

def initialize_log_directory():
    """
    Chức năng 4: Tự động khởi tạo thư mục log, bẫy lỗi trùng thư mục (Edge Case 3).
    """
    print("\n----- KHỞI TẠO THƯ MỤC HỆ THỐNG -----")
    dir_name = "aviation_logs"
    
    if not os.path.exists(dir_name):
        print(f"[SYSTEM] Thư mục '{dir_name}' chưa tồn tại. Đang tiến hành khởi tạo...")
        os.mkdir(dir_name)
        print("[SYSTEM] Tạo thư mục thành công!")
    else:
        print("[SYSTEM] Thư mục đã tồn tại, bỏ qua bước khởi tạo.")