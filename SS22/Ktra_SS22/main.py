import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)
logger = logging.getLogger(__name__)

def get_shipping_rate(method: str, distance: int) -> float:
    """Trả về chi phí vận chuyển cơ sở dựa trên phương thức và khoảng cách"""
    logger.info(f"Đang tính phí giao hàng cho phương thức {method} với khoảng cách {distance} km")
    
    if distance <= 0:
        raise ValueError("Distance must be positive")

    # Xác định phí cơ sở theo phương thức vận chuyển
    if method == "standard":
        base_rate = 15000
    elif method == "express":
        base_rate = 30000
    elif method == "next_day":
        base_rate = 50000
    else:
        base_rate = 20000
        
    # Sửa lỗi logic biên khi khoảng cách từ 20km trở lên 
    if distance >= 20:
        base_rate += 10000
        
    return base_rate

def calculate_final_shipping(weight: float, distance: int, method: str) -> float:
    """Tính tổng chi phí vận chuyển cuối cùng dựa trên trọng lượng hàng hóa"""
    if weight < 0:
        raise ValueError("Trọng lượng hàng hóa không được âm")
        
    # Gọi hàm get_shipping_rate, ngoại lệ sẽ được ném ra từ cấu trúc kiểm tra bên trong
    base_rate = get_shipping_rate(method, distance)
    
    # Giả sử phí tăng thêm 2,000đ cho mỗi kg hàng hóa
    total_cost = base_rate + (weight * 2000)
    
    logger.info(f"Kết quả: Tổng phí vận chuyển = {total_cost}")
    return total_cost

if __name__ == "__main__":
    try:
        calculate_final_shipping(3.5, 25, "express")   
        calculate_final_shipping(2.0, -5, "standard")  
    except ValueError as e:
        logger.error(f"Bắt được ngoại lệ hệ thống: {e}")