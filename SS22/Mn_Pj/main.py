import logging

# ==========================================
# CẤU HÌNH HỆ THỐNG LOGGING (YÊU CẦU ĐẶC TẢ)
# ==========================================
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


# ==========================================
# CÁC HÀM XỬ LÝ NGHIỆP VỤ (CORE FUNCTIONS)
# ==========================================

def show_devices(devices: list) -> None:
    """Chức năng 1: Hiển thị danh sách thiết bị dưới dạng bảng căn lề thẳng hàng."""
    if not devices:
        logging.info("Yêu cầu hiển thị danh sách: Hệ thống trống.")
        print("\n[Thông báo]: Hệ thống trống. Chưa có thiết bị nào được giám sát.")
        return

    logging.info("Xuất báo cáo danh sách thiết bị giám sát.")
    print("\n" + "="*80)
    print(f"{'MÃ TB':<10}{'VỊ TRÍ XƯỞNG':<25}{'CHỈ SỐ CŨ':<12}{'CHỈ SỐ MỚI':<12}{'TRẠNG THÁI':<12}")
    print("-" * 80)
    for dev in devices:
        print(f"{dev['id']:<10}{dev['location']:<25}{dev['old_index']:<12}{dev['new_index']:<12}{dev['status']:<12}")
    print("="*80)


def update_indices(devices: list) -> None:
    """Chức năng 2: Cập nhật chỉ số điện tiêu thụ (Check-in số liệu)."""
    print("\n--- CẬP NHẬT CHỈ SỐ ĐIỆN ---")
    device_id = input("Nhập mã thiết bị: ").strip()

    target_device = None
    for dev in devices:
        if dev['id'] == device_id:
            target_device = dev
            break

    if not target_device:
        print(f"[Lỗi] (ERR-E01): Mã thiết bị này không tồn tại trong danh sách hệ thống.")
        return

    # Validate chỉ số cũ (Phải là số nguyên >= 0)
    while True:
        try:
            old_idx = int(input("Nhập chỉ số cũ: "))
            if old_idx < 0:
                print("[Lỗi]: Chỉ số cũ phải lớn hơn hoặc bằng 0. Vui lòng nhập lại.")
                continue
            break
        except ValueError:
            print("[Lỗi]: Chỉ số phải là một số nguyên hợp lệ. Vui lòng nhập lại.")

    # Validate chỉ số mới (Phải là số nguyên >= chỉ số cũ)
    while True:
        try:
            new_idx = int(input("Nhập chỉ số mới: "))
            if new_idx < 0:
                print("[Lỗi]: Chỉ số mới phải lớn hơn hoặc bằng 0. Vui lòng nhập lại.")
                continue
            if new_idx < old_idx:
                print(f"[Lỗi] (ERR-E02): Chỉ số mới ({new_idx}) không được nhỏ hơn chỉ số cũ ({old_idx}). Vui lòng nhập lại.")
                continue
            break
        except ValueError:
            print("[Lỗi]: Chỉ số phải là một số nguyên hợp lệ. Vui lòng nhập lại.")

    target_device['old_index'] = old_idx
    target_device['new_index'] = new_idx
    logging.info(f"Cập nhật số liệu thành công cho thiết bị {device_id} (Cũ: {old_idx} | Mới: {new_idx}).")
    print(f"[Thành công]: Thiết bị {device_id} đã được cập nhật số liệu mới.")


def activate_overload_warning(devices: list) -> None:
    """Chức năng 3: Kích hoạt trạng thái cảnh báo quá tải."""
    print("\n--- KÍCH HOẠT CẢNH BÁO QUÁ TẢI ---")
    device_id = input("Nhập mã thiết bị cần duyệt: ").strip()

    target_device = None
    for dev in devices:
        if dev['id'] == device_id:
            target_device = dev
            break

    if not target_device:
        print(f"[Lỗi] (ERR-E01): Không tìm thấy mã thiết bị {device_id} trong hệ thống.")
        return

    if target_device['status'] == 'Overload':
        print(f"[Lỗi] (ERR-E04): Thao tác bị hủy! Thiết bị {device_id} này đã được kích hoạt trạng thái OVERLOAD từ trước!")
        return

    consumption = target_device['new_index'] - target_device['old_index']

    if consumption > 5000:
        target_device['status'] = 'Overload'
        # Thay thế lệnh in báo cáo nội bộ bằng log mức WARNING
        logging.warning(f"Thiết bị {device_id} tại {target_device['location']} vượt ngưỡng an toàn ({consumption} kWh) -> Chuyển sang OVERLOAD!")
        print(f"[Thành công]: Thiết bị {device_id} đã được kích hoạt trạng thái OVERLOAD!")
    else:
        logging.info(f"Duyệt thiết bị {device_id}: Lượng tiêu thụ ({consumption} kWh) nằm trong mức an toàn.")
        print(f"[Thông báo]: Lượng tiêu thụ hiện tại là {consumption} kWh (Dưới mốc cảnh báo 5000 kWh).")


def calculate_energy_financials(devices: list) -> tuple:
    """Chức năng 4: Hàm tính toán tài chính (Chỉ thực hiện tính toán và return dạng Tuple)."""
    total_consumption = 0
    for dev in devices:
        consumption = dev['new_index'] - dev['old_index']
        if consumption > 0:
            total_consumption += consumption

    base_rate = 3000  
    discount_rate = 0.0

    if total_consumption >= 50000:
        discount_rate = 0.03  

    total_cost_before_discount = total_consumption * base_rate
    total_discount_amount = total_cost_before_discount * discount_rate
    final_cost = total_cost_before_discount - total_discount_amount

    return total_consumption, int(discount_rate * 100), int(final_cost)



def main():
    # Khởi tạo dữ liệu gốc phục vụ chạy demo
    devices = [
        {'id': 'M01', 'location': 'Mechanical Shop A', 'old_index': 1200, 'new_index': 4500, 'status': 'Normal'},
        {'id': 'M02', 'location': 'Assembly Line B', 'old_index': 2300, 'new_index': 8500, 'status': 'Overload'},
        {'id': 'M03', 'location': 'Packaging Area C', 'old_index': 1000, 'new_index': 52000, 'status': 'Normal'}
    ]

    while True:
        print("\n===== SMART ENERGY MONITOR MENU =====")
        print("1. Xem danh sách thiết bị giám sát")
        print("2. Cập nhật chỉ số điện tiêu thụ")
        print("3. Kích hoạt trạng thái cảnh báo quá tải")
        print("4. Tính tổng lượng điện & Chi phí năng lượng")
        print("5. Thoát chương trình")
        
        choice = input("Mời chọn chức năng (1-5): ").strip()

        match choice:
            case '1':
                show_devices(devices)
            case '2':
                update_indices(devices)
            case '3':
                activate_overload_warning(devices)
            case '4':
                total_cons, discount, final_price = calculate_energy_financials(devices)
                logging.info(f"Kết xuất báo cáo tài chính - Tổng tiêu thụ: {total_cons} kWh | Chiết khấu: {discount}%")
                
                print("\n--- BÁO CÁO TÀI CHÍNH NĂNG LƯỢNG ---")
                print(f"+ Tổng lượng điện tiêu thụ thực tế: {total_cons:,} kWh")
                print(f"+ Tỷ lệ chiết khấu áp dụng từ nhà nước: {discount}%")
                print(f"+ Tổng chi phí năng lượng phải trả sau chiết khấu: {final_price:,} VND")
            case '5':
                logging.info("Hệ thống đóng. Người dùng thoát chương trình.")
                print("\nCảm ơn bạn đã sử dụng hệ thống Smart Energy Monitor. Tạm biệt!")
                break
            case _:
                print("[Lỗi]: Chức năng không tồn tại. Vui lòng chỉ chọn từ 1 đến 5.")


if __name__ == '__main__':
    main()