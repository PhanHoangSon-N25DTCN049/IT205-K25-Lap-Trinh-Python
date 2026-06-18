class NetflixAccount:
    """
    Lớp quản lý tài khoản Netflix áp dụng các tính chất OOP Core.
    """
    # Class Attributes
    platform_name = "Netflix"
    max_profiles = 5

    def __init__(self, email):
        self.email = email
        self.__password = ""  # Private attribute via Name Mangling
        self.__plan = "Basic"  # Private attribute via Name Mangling
        self.profiles = []

    @property
    def password(self):
        """Getter cho password: Luôn ẩn danh dữ liệu khi đọc."""
        return "********"

    @password.setter
    def password(self, new_password):
        """Setter cho password: Kiểm tra điều kiện bảo mật nghiêm ngặt."""
        if len(new_password) < 6:
            raise ValueError("Password is too short")
        self.__password = new_password

    @property
    def plan(self):
        """Getter cho plan: Thuộc tính Read-only, không có setter."""
        return self.__plan

    @staticmethod
    def validate_email(email):
        """Kiểm tra email hợp lệ phải chứa ký tự '@' và dấu '.'."""
        return "@" in email and "." in email

    @classmethod
    def update_max_profiles(cls, new_limit):
        """Cập nhật giới hạn số lượng Profile trên toàn hệ thống toàn cầu."""
        cls.max_profiles = new_limit

    def add_profile(self, profile_name):
        """Thêm người xem mới nếu chưa đạt giới hạn tối đa."""
        if len(self.profiles) >= NetflixAccount.max_profiles:
            print("Đã đạt giới hạn số lượng Profile trên tài khoản này.")
            return
        self.profiles.append(profile_name)
        print(f"Đã thêm người xem: '{profile_name}' thành công.")

    def upgrade_plan(self, new_plan):
        """Phương thức hợp lệ duy nhất để thay đổi gói cước dịch vụ."""
        valid_plans = ["Basic", "Standard", "Premium"]
        if new_plan in valid_plans:
            self.__plan = new_plan
            print(f"Nâng cấp gói cước lên '{new_plan}' thành công.")
        else:
            print("Gói cước không hợp lệ! Chỉ chọn: Basic, Standard, Premium.")

    def display_info(self):
        """In thông tin chi tiết của tài khoản hiện tại."""
        print("\n--- THÔNG TIN TÀI KHOẢN ---")
        print(f"Nền tảng: {self.platform_name}")
        print(f"Email: {self.email}")
        print(f"Mật khẩu: {self.password}")  # Gọi qua property getter
        print(f"Gói cước: {self.plan}")      # Gọi qua property getter
        print(f"Danh sách người xem: {self.profiles if self.profiles else 'Chưa có Profile'}")
        print("---------------------------")


def main():
    current_account = None

    while True:
        print("\n===== NETFLIX ACCOUNT MANAGER =====")
        print("1. Đăng ký tài khoản mới")
        print("2. Xem thông tin tài khoản")
        print("3. Thêm người xem")
        print("4. Nâng cấp gói cước")
        print("5. Cập nhật chính sách Netflix (Admin)")
        print("6. Thoát chương trình")
        print("===================================")
        
        choice = input("Chọn chức năng (1-6): ").strip()

        match choice:
            case "1":
                email = input("Nhập Email: ").strip()
                if not NetflixAccount.validate_email(email):
                    print("Lỗi: Email không hợp lệ, vui lòng chứa ký tự '@' và '.'.")
                    continue
                
                password = input("Nhập Mật khẩu (tối thiểu 6 ký tự): ")
                try:
                    # Khởi tạo đối tượng và kiểm tra pass qua setter
                    account = NetflixAccount(email)
                    account.password = password
                    current_account = account
                    print("Đăng ký tài khoản Netflix thành công!")
                except ValueError as e:
                    print(f"Lỗi bảo mật mật khẩu: {e}")

            case "2":
                if current_account is None:
                    print("Cảnh báo: Vui lòng đăng ký tài khoản trước (Chức năng 1).")
                else:
                    current_account.display_info()

            case "3":
                if current_account is None:
                    print("Cảnh báo: Vui lòng đăng ký tài khoản trước (Chức năng 1).")
                else:
                    profile_name = input("Nhập tên Profile mới (VD: Bo Me, Con Gai): ").strip()
                    if profile_name:
                        current_account.add_profile(profile_name)
                    else:
                        print("Tên người xem không được để trống.")

            case "4":
                if current_account is None:
                    print("Cảnh báo: Vui lòng đăng ký tài khoản trước (Chức năng 1).")
                else:
                    print("Các gói cước hiện có: Basic, Standard, Premium")
                    new_plan = input("Nhập gói cước muốn đổi: ").strip()
                    current_account.upgrade_plan(new_plan)

            case "5":
                try:
                    new_limit = int(input("Nhập số lượng Profile tối đa mới cho toàn hệ thống: "))
                    if new_limit < 0:
                        print("Số lượng giới hạn không thể là số âm.")
                        continue
                    NetflixAccount.update_max_profiles(new_limit)
                    print(f"Đã cập nhật giới hạn Profile toàn hệ thống thành {NetflixAccount.max_profiles}.")
                except ValueError:
                    print("Vui lòng nhập vào một số nguyên hợp lệ.")

            case "6":
                print("Đã thoát hệ thống quản lý Netflix. Tạm biệt!")
                break

            case _:
                print("Chức năng lựa chọn không hợp lệ. Vui lòng chọn lại từ 1 đến 6.")

if __name__ == "__main__":
    main()