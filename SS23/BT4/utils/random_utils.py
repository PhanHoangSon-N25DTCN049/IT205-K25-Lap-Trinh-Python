import random
import string

def generate_assignment_code():
    """
    Sinh ngẫu nhiên mã bài tập theo định dạng PY-[4 ký tự chữ hoa hoặc số].
    Sử dụng 2 thư viện chuẩn là random và string.
    """
    # Tập hợp các ký tự gồm chữ cái in hoa và các chữ số từ 0-9
    pool = string.ascii_uppercase + string.digits
    random_chars = "".join(random.choices(pool, k=4))
    
    print("\n--- SINH MÃ BÀI TẬP ---")
    print(f"Mã bài tập của bạn là: PY-{random_chars}")