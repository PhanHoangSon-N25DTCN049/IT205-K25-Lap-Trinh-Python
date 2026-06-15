import logging
import os

logging.basicConfig(
    filename="momo_transactions.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def check_and_deposit(current_balance: int, amount: int) -> int:
    """Tính toán số dư mới khi nạp tiền.

    Ném ra lỗi ValueError nếu số tiền không hợp lệ.
    """
    if amount <= 0:
        raise ValueError(f"Số tiền nạp phải lớn hơn 0. Nhận được: {amount}")

    return current_balance + amount


def check_and_transfer(current_balance: int, amount: int) -> int:
    """Tính toán số dư mới sau khi chuyển tiền.

    Ném ra lỗi ValueError nếu vi phạm quy tắc nghiệp vụ.
    """
    if amount <= 0:
        raise ValueError(f"Số tiền chuyển phải lớn hơn 0. Nhận được: {amount}")

    if amount > current_balance:
        raise ValueError(
            f"Số dư không đủ. Cần: {amount}, Hiện có: {current_balance}"
        )

    return current_balance - amount

def display_menu():
    """Hiển thị menu chức năng."""
    print("\n========== VÍ MOMO GIẢ LẬP (FUNCTIONAL) ==========")
    print("1. Nạp tiền vào ví")
    print("2. Chuyển tiền")
    print("3. Xem lịch sử giao dịch (Đọc file log)")
    print("4. Xem số dư hiện tại")
    print("5. Thoát chương trình")
    print("==================================================")


def handle_deposit(current_balance: int) -> int:
    """Xử lý luồng nạp tiền và trả về số dư mới sau khi xử lý."""
    print("\n--- NẠP TIỀN VÀO VÍ ---")
    user_input = input("Nhập số tiền cần nạp: ")

    try:
        amount = int(user_input)

        # Gọi hàm xử lý tính toán ở Tầng 2
        new_balance = check_and_deposit(current_balance, amount)

        # Ghi log nghiệp vụ và báo thành công
        logging.info(
            f"Deposit successful: +{amount} VND. Current Balance: {new_balance}"
        )
        print(f"\nNạp tiền thành công: +{amount:,} VND")
        print(f"Số dư hiện tại: {new_balance:,} VND")

        return new_balance

    except ValueError as e:
        # Bắt cả lỗi nhập chữ của int() và lỗi số âm của check_and_deposit()
        logging.error(f"Lỗi nạp tiền: {e}")
        print(f"\nGiao dịch thất bại. Chi tiết: {e}")
        return current_balance  # Thất bại thì giữ nguyên số dư cũ


def handle_transfer(current_balance: int) -> int:
    """Xử lý luồng chuyển tiền và trả về số dư mới sau khi xử lý."""
    print("\n--- CHUYỂN TIỀN ---")
    phone = input("Nhập số điện thoại người nhận: ").strip()

    # Kiểm tra nhanh số điện thoại bằng Fail-Fast
    if len(phone) != 10 or not phone.isdigit():
        print("\nLỗi: Số điện thoại người nhận phải đúng định dạng 10 số.")
        return current_balance

    user_input = input("Nhập số tiền cần chuyển: ")

    try:
        amount = int(user_input)

        # Tính năng cảnh báo giao dịch lớn
        if amount >= 10000000:
            logging.warning(
                f"Phát hiện giao dịch giá trị cao: {amount} VND đến số {phone}"
            )

        # Gọi hàm xử lý tính toán ở Tầng 2
        new_balance = check_and_transfer(current_balance, amount)

        # Ghi log nghiệp vụ và báo thành công
        logging.info(
            f"Chuyển khoản thành công: -{amount} VND đến {phone}. Số dư hiện tại: {new_balance}"
        )
        print(f"\nChuyển tiền thành công tới số điện thoại {phone}.")
        print(f"Số tiền đã chuyển: {amount:,} VND")
        print(f"Số dư còn lại: {new_balance:,} VND")

        return new_balance

    except ValueError as e:
        logging.error(f"Lỗi chuyển tiền: {e}")
        print(f"\nGiao dịch thất bại. Chi tiết: {e}")
        return current_balance


def handle_show_history():
    """Đọc và in file log ra màn hình."""
    print("\n--- LỊCH SỬ GIAO DỊCH ---")
    if (
        not os.path.exists("momo_transactions.log")
        or os.path.getsize("momo_transactions.log") == 0
    ):
        print("Chưa có lịch sử giao dịch nào trong hệ thống.")
        return

    with open("momo_transactions.log", "r", encoding="utf-8") as file:
        print(file.read().strip())


def main():
    balance = 0

    while True:
        display_menu()
        choice = input("Chọn chức năng (1-5): ").strip()

        match choice:
            case "1":
                balance = handle_deposit(balance)
            case "2":
                balance = handle_transfer(balance)
            case "3":
                handle_show_history()
            case "4":
                print("\n--- SỐ DƯ VÍ MOMO ---")
                print(f"Số dư hiện tại: {balance:,} VND")
                logging.info(f"Đã kiểm tra số dư. Số dư hiện tại: {balance}")
            case "5":
                logging.info("System shutdown")
                print("\nCảm ơn bạn đã sử dụng dịch vụ MoMo.")
                break
            case _:
                print("\nLựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 5.")


if __name__ == "__main__":
    main()