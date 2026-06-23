from __future__ import annotations
from abc import ABC, abstractmethod;
class BaseEmployee(ABC):
    company_name = "Rikkei Education";
    base_salary_rate = 3000000;
    def __init__(self, name: str, employee_code:str):
        self.__working_hours = 0;
        self.name = name;
        self.employee_code = employee_code;
    
    @property 
    def working_hours(self):
        return self.__working_hours;
    
    @staticmethod
    def validate_employee_code(emp_code):
        if len(emp_code) != 10 or emp_code[:3] != "RKE":
            return False
        return True
    
    @classmethod 
    def update_base_salary_rate(cls, new_rate):
        if new_rate <= 0:
            raise ValueError("Số liệu cập nhật không được nhỏ hơn hoặc bằng 0")
        cls.base_salary_rate = new_rate;
        
    
    @abstractmethod 
    def calculate_salary(self):
        pass;
    
    @abstractmethod 
    def update_kpi(self, progress):
        pass;
    
    def __add__(self, other):
        return self.working_hours + other.working_hours;
    
    def __lt__(self, other):
        return self.working_hours < other.working_hours;
    
class Lecturer(BaseEmployee):
    def __init__(self, name, employee_code ):
        super().__init__(name, employee_code);
        self.teaching_slots = 0;
        self.kpi_percentage = 0;
        
    def calculate_salary(self):
        return (self.working_hours * self.base_salary_rate) + (self.teaching_slots * 500000);
    
    def update_kpi(self, progress):
        if progress <= 0:
            raise ValueError("Số liệu cập nhật không được nhỏ hơn hoặc bằng 0");
        self.kpi_percentage = progress;
        
    def conduct_class(self):
        self.teaching_slots += 1;
        self._BaseEmployee__working_hours += 2;
        print("Ghi nhận thành công! Thầy/Cô đã hoàn thành thêm 1 ca dạy.");
        
class AdmissionStaff(BaseEmployee):
    def __init__(self, name, employee_code):
        super().__init__(name, employee_code)
        self.revenue_generated = 0;
        self.kpi_target = 0;
        
    def calculate_salary(self):
        return (self.working_hours * self.base_salary_rate) + (self.revenue_generated * 0.05);
    
    def update_kpi(self, progress):
        if progress <= 0:
            raise ValueError("Số liệu cập nhật không được nhỏ hơn hoặc bằng 0");
        self.revenue_generated += progress;
            
class HybridManager(Lecturer, AdmissionStaff):
    def __init__(self, name, employee_code):
        super().__init__(name, employee_code);
        self.revenue_generated = 0;
        self.kpi_target = 0;
    
    def calculate_salary(self):
        return (self.working_hours * self.base_salary_rate) + (self.teaching_slots * 500000) + (self.revenue_generated * 0.05)
    
    def update_kpi(self, progress):
        if progress <= 0:
            raise ValueError("Số liệu cập nhật không được nhỏ hơn hoặc bằng 0")
        self.revenue_generated += progress;
        

# Định nghĩa thêm 2 lớp ngân hàng để phục vụ Chức năng 6 (Duck Typing)
class VietcombankCorporateService:
    def transfer_salary(self, employee, amount):
        print("[Hệ thống VCB Corporate]: Đang kết nối tới cổng chi trả Rikkei...")
        print("Xác thực đối tác bằng Duck Typing thành công!")
        print(f"Ngân hàng đối tác đã giải ngân thành công số tiền: {amount:,} VND tới nhân sự {employee.employee_code}.")

class TechcombankCorporateService:
    def transfer_salary(self, employee, amount):
        print("[Hệ thống TCB Corporate]: Đang thiết lập đường truyền mã hóa an toàn...")
        print("Xác thực đối tác bằng Duck Typing thành công!")
        print(f"Ngân hàng đối tác đã giải ngân thành công số tiền: {amount:,} VND tới nhân sự {employee.employee_code}.")


def add_input(choice):
    while True:
        id = input("Nhập mã nhân sự 10 ký tự: ")
        if BaseEmployee.validate_employee_code(id):
            break;
        print("Mã nhân sự không hợp lệ! Phải gồm đúng 10 ký tự và bắt đầu bằng RKE.")
    while True:
        name = input("Nhập họ và tên: ");
        if name.strip():
            name = name.strip().upper()
            break
        print("Tên nhân sự không được bỏ trống")
    return name,id

def main():
    employees = []
    current_employee = None
    
    while True:
        choice = input("""===== RIKKEI EDUCATION HR SIMULATOR PRO =====
1. Tuyển dụng nhân sự mới (Chọn loại hợp đồng nhân sự)
2. Xem thông tin & Kiểm tra thứ tự kế thừa (MRO)
3. Ghi nhận công nhật & Cập nhật KPI (Tính đa hình)
4. Tổng hợp quỹ lương và ngân sách chi trả
5. Kiểm tra gộp giờ làm việc & So sánh hiệu suất (Overloading)
6. Giải ngân lương qua Cổng thanh toán đối tác (Duck Typing)
7. Thoát chương trình
==============================================
Chọn chức năng (1-7): """)
        
        match choice:
            case "1":
                choice_add = input("""
--- CHỌN LOẠI NHÂN SỰ KHỞI TẠO ---
1. Lecturer (Giảng viên chuyên trách)
2. Admission Staff (Nhân viên Tuyển sinh)
3. Hybrid Manager (Quản lý kiêm Giảng dạy)
Chọn loại nhân sự (1-3): """)
                match choice_add:
                    case "1":
                        name, id = add_input()
                        current_employee = Lecturer(name, id)
                        employees.append(current_employee)
                        print("Tuyển dụng Giảng viên chuyên trách thành công!")
                        print(f"Tên nhân sự: {current_employee.name}\n")
                    case "2":
                        name, id = add_input()
                        current_employee = AdmissionStaff(name, id)
                        employees.append(current_employee)
                        print("Tuyển dụng nhân viên Tuyển sinh thành công!")
                        print(f"Tên nhân sự: {current_employee.name}\n")
                    case "3":
                        name, id = add_input()
                        current_employee = HybridManager(name, id)
                        employees.append(current_employee)
                        print("Tuyển dụng Quản lý kiêm Giảng dạy thành công!")
                        print(f"Tên nhân sự: {current_employee.name}\n")
                    case _:
                        print("Lỗi lựa chọn!\n")

            case "2":
                if current_employee is None:
                    print("Hiện tại công ty chưa có nhân sự nào!\n")
                    continue
                position = type(current_employee).__name__
                print("--- THÔNG TIN NHÂN SỰ HIỆN TẠI ---")
                print(f"Loại nhân sự: {position}")
                print(f"Tổ chức: {current_employee.company_name}")
                print(f"Mã nhân sự: {current_employee.employee_code}")
                print(f"Họ và tên: {current_employee.name}")
                print(f"Số giờ làm việc: {current_employee.working_hours} giờ")
                if isinstance(current_employee, Lecturer):
                    print(f"Số ca đã dạy: {current_employee.teaching_slots} ca")
                if isinstance(current_employee, AdmissionStaff):
                    print(f"Doanh số mang về: {current_employee.revenue_generated:,} VND")
                    
                mro_list = [cls.__name__ for cls in type(current_employee).__mro__]
                print(f"Thứ tự kế thừa (MRO): {' -> '.join(mro_list)}")
                print()

            case "3":
                if current_employee is None:
                    print("Hiện tại công ty chưa có nhân sự nào!\n")
                    continue
                
                print("--- GHI NHẬN CÔNG NHẬT & HIỆU SUẤT ---")
                print("1. Ghi nhận tham gia đứng lớp (Chỉ dành cho Giảng viên/Hybrid)")
                print("2. Cập nhật tiến độ KPI / Doanh số")
                task_choice = input("Chọn tác vụ (1-2): ")
                
                match task_choice:
                    case "1":
                        # Chỉ cho phép Lecturer hoặc HybridManager tham gia đứng lớp
                        if hasattr(current_employee, 'conduct_class'):
                            current_employee.conduct_class()
                            print(f"Số ca dạy hiện tại: {current_employee.teaching_slots} ca.")
                            print("Số giờ làm việc tích lũy: +2 giờ.")
                        else:
                            print("Lỗi: Nhân viên Tuyển sinh không có chức năng đứng lớp!")
                    case "2":
                        try:
                            if isinstance(current_employee, HybridManager) or isinstance(current_employee, AdmissionStaff):
                                progress = float(input("Nhập giá trị doanh số hợp đồng mới mang về: "))
                                current_employee.update_kpi(progress)
                                print("Cập nhật KPI thành công!")
                                print(f"Doanh số tích lũy mới: {current_employee.revenue_generated:,} VND.")
                            else: # Giảng viên thuần túy
                                progress = float(input("Nhập tỷ lệ hoàn thành khung chương trình (%): "))
                                current_employee.update_kpi(progress)
                                print(f"Cập nhật KPI thành công! Tiến độ hiện tại: {current_employee.kpi_percentage}%.")
                        except ValueError as e:
                            print(f"Lỗi: {e}")
                    case _:
                        print("Lựa chọn tác vụ không hợp lệ!")
                print()

            case "4":
                if current_employee is None:
                    print("Hiện tại công ty chưa có nhân sự nào!\n")
                    continue
                
                position = type(current_employee).__name__
                base_salary = current_employee.working_hours * current_employee.base_salary_rate
                total_salary = current_employee.calculate_salary()
                allowance_bonus = total_salary - base_salary
                
                print("--- CHI TIẾT QUỸ LƯƠNG NHÂN SỰ ---")
                print(f"Nhân sự: {current_employee.name} (Loại: {position})")
                print(f"Mức lương cơ sở hệ thống: {current_employee.base_salary_rate:,} VND")
                print(f"Số giờ làm việc tích lũy: {current_employee.working_hours} giờ")
                print(f"Lương cứng tính theo giờ: {base_salary:,} VND")
                print(f"Phụ cấp ca dạy + Hoa hồng tuyển sinh tích hợp: {allowance_bonus:,} VND")
                print(f"Tổng lương thực nhận tháng này: {total_salary:,} VND\n")

            case "5":
                if current_employee is None or len(employees) < 2:
                    print("Hệ thống cần ít nhất 2 nhân sự để thực hiện so sánh đối ứng!\n")
                    continue
                
                print("--- ĐỒNG BỘ & SO SÁNH GIỜ CÔNG (OPERATOR OVERLOADING) ---")
                print(f"Nhân sự hiện tại (A): {current_employee.name} (Giờ công: {current_employee.working_hours} giờ)")
                print("Danh sách nhân sự đối ứng trong hệ thống:")
                
                # Hiển thị danh sách nhân sự ngoại trừ chính mình để lựa chọn
                valid_opponents = [emp for emp in employees if emp.employee_code != current_employee.employee_code]
                for idx, emp in enumerate(valid_opponents):
                    print(f"{idx + 1}. Mã: {emp.employee_code} - Tên: {emp.name} (Giờ công: {emp.working_hours} giờ)")
                
                try:
                    opp_choice = int(input("Chọn nhân sự đối ứng (B) từ danh sách: ")) - 1
                    if 0 <= opp_choice < len(valid_opponents):
                        opponent = valid_opponents[opp_choice]
                        
                        # Sử dụng nạp chồng toán tử __lt__
                        if current_employee < opponent:
                            print("[Kết quả So sánh (__lt__)]: Giờ công cống hiến của nhân sự A ÍT HƠN nhân sự B.")
                        else:
                            print("[Kết quả So sánh (__lt__)]: Giờ công cống hiến của nhân sự A KHÔNG ÍT HƠN nhân sự B.")
                        
                        # Sử dụng nạp chồng toán tử __add__
                        total_hours = current_employee + opponent
                        print(f"[Kết quả Tổng hợp (__add__)]: Tổng số giờ làm việc của cả 2 nhân sự là: {total_hours} giờ.")
                    else:
                        print("Lựa chọn nhân sự không nằm trong danh sách!")
                except ValueError:
                    print("Vui lòng nhập vào một số nguyên hợp lệ!")
                print()

            case "6":
                if current_employee is None:
                    print("Hiện tại công ty chưa có nhân sự nào!\n")
                    continue
                
                print("--- CHI TRẢ LƯƠNG QUA CỔNG ĐỐI TÁC TRUNG GIAN ---")
                print("1. Chi trả qua tài khoản Doanh nghiệp Vietcombank")
                print("2. Chi trả qua tài khoản Doanh nghiệp Techcombank")
                bank_choice = input("Chọn cổng ngân hàng (1-2): ")
                
                payment_service = None
                match bank_choice:
                    case "1":
                        payment_service = VietcombankCorporateService()
                    case "2":
                        payment_service = TechcombankCorporateService()
                    case _:
                        print("Cổng ngân hàng không hỗ trợ!")
                        continue
                
                def execute_payroll(service, employee, amount):
                    try:
                        if not hasattr(service, 'transfer_salary'):
                            raise AttributeError
                        service.transfer_salary(employee, amount)
                    except AttributeError:
                        print("Lỗi: Cổng dịch vụ ngân hàng doanh nghiệp không hợp lệ hoặc chưa được liên kết liên thông kỹ thuật.")
                
                amount_to_pay = current_employee.calculate_salary()
                execute_payroll(payment_service, current_employee, amount_to_pay)
                print()

            case "7":
                print("Cảm ơn đã sử dụng hệ thống Quản lý Nhân sự Rikkei Education Pro!")
                break
                
            case _:
                print("Chức năng không hợp lệ! Vui lòng chọn lại từ 1-7.\n")