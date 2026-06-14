import unittest
# Import hàm xử lý tính tổng tiền từ file hệ thống chính
from main import calculate_total_revenue

class TestTicketRevenue(unittest.TestCase):
    
    def test_mixed_tickets_revenue(self):
        """Test Case 1: Danh sách có cả vé Booked và Cancelled -> Hàm trả về đúng tổng tiền vé Booked"""
        mock_tickets = [
            {"ticket_id": "T01", "price": 500.0, "status": "Booked"},
            {"ticket_id": "T02", "price": 300.0, "status": "Cancelled"},
            {"ticket_id": "T03", "price": 400.0, "status": "Booked"}
        ]
        # Chỉ tính tiền vé T01 và T03: 500.0 + 400.0 = 900.0
        self.assertEqual(calculate_total_revenue(mock_tickets), 900.0)

    def test_empty_tickets_revenue(self):
        """Test Case 2: Danh sách trống [] -> Hàm phải trả về giá trị mặc định là 0.0"""
        empty_list = []
        self.assertEqual(calculate_total_revenue(empty_list), 0.0)

if __name__ == "__main__":
    unittest.main()