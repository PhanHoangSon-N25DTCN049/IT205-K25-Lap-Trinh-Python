from abc import ABC, abstractmethod

# ==================== THIẾT KẾ CLASS & OBJECT ====================

class Employee(ABC):
    """Lớp trừu tượng đại diện cho một nhân viên nói chung."""
    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name

    def display_info(self, employee_type):
        """Hiển thị thông tin cơ bản của nhân viên."""
        print(f"Mã NV: {self.employee_id} | Họ tên: {self.name} | Loại: {employee_type}")

    @abstractmethod
    def calculate_salary(self):
        """Phương thức trừu tượng bắt buộc các lớp con phải ghi đè."""
        pass


class FullTimeEmployee(Employee):
    """Nhân viên toàn thời gian."""
    def __init__(self, employee_id, name, base_salary, bonus):
        super().__init__(employee_id, name)
        self.base_salary = base_salary
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus


class PartTimeEmployee(Employee):
    """Nhân viên bán thời gian."""
    def __init__(self, employee_id, name, working_hours, hourly_rate):
        super().__init__(employee_id, name)
        self.working_hours = working_hours
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.working_hours * self.hourly_rate


class InternEmployee(Employee):
    """Thực tập sinh."""
    def __init__(self, employee_id, name, allowance):
        super().__init__(employee_id, name)
        self.allowance = allowance

    def calculate_salary(self):
        return self.allowance


# ==================== CÁC HÀM CHỨC NĂNG NGHIỆP VỤ ====================

def display_employees(employees_list):
    """Chức năng 1: Xem danh sách nhân viên."""
    print("\n--- DANH SÁCH NHÂN VIÊN ---")
    for emp in employees_list:
        # Xác định chuỗi hiển thị loại nhân viên tương ứng
        if isinstance(emp, FullTimeEmployee):
            emp_type = "Full-time"
        elif isinstance(emp, PartTimeEmployee):
            emp_type = "Part-time"
        else:
            emp_type = "Intern"
        
        emp.display_info(emp_type)


def display_salaries(employees_list):
    """Chức năng 2: Tính và hiển thị bảng lương toàn bộ nhân viên (Áp dụng Tính Đa Hình)."""
    print("\n--- BẢNG LƯƠNG NHÂN VIÊN ---")
    for emp in employees_list:
        # Tuyệt đối không dùng if/match-case để phân loại công thức tính lương.
        # Tính đa hình tự động gọi đúng phương thức tính của từng Class con.
        salary = emp.calculate_salary()
        print(f"{emp.employee_id} | {emp.name:<12} | Lương: {salary:,.0f} VND")


# ==================== ĐIỀU HƯỚNG CHƯƠNG TRÌNH (MENU) ====================

def main():
    # Khởi tạo Mock Data theo đúng yêu cầu đề bài
    employees = [
        FullTimeEmployee("E001", "Nguyen Van A", 15000000, 3000000),
        PartTimeEmployee("E002", "Tran Thi B", 80, 50000),
        InternEmployee("E003", "Le Van C", 3000000)
    ]

    while True:
        print("\n=== EMPLOYEE SALARY MANAGER ===")
        print("1. Xem danh sách nhân viên")
        print("2. Tính lương toàn bộ nhân viên")
        print("3. Thoát chương trình")
        print("================================")
        
        choice = input("Chọn chức năng (1-3): ").strip()

        match choice:
            case "1":
                display_employees(employees)
            case "2":
                display_salaries(employees)
            case "3":
                print("Cảm ơn bạn đã sử dụng Employee Salary Manager!")
                break
            case _:
                print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main()