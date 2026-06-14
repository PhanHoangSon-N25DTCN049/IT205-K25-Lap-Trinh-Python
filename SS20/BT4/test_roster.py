import unittest
from main import calculate_actual_pay

class TestPlayerPayroll(unittest.TestCase):
    
    def test_active_player_pay(self):
        """Test Case 1: Tuyển thủ đang Active phải nhận đủ 100% lương gốc"""
        player_active = {
            "player_id": "P01",
            "name": "Faker",
            "role": "Mid Lane",
            "salary": 5000.0,
            "status": "Active"
        }
        # Lương gốc 5000.0 -> Thực lĩnh phải bằng 5000.0
        self.assertEqual(calculate_actual_pay(player_active), 5000.0)

    def test_benched_player_pay(self):
        """Test Case 2: Tuyển thủ đang Benched (Dự bị) chỉ nhận 50% lương gốc"""
        player_benched = {
            "player_id": "P03",
            "name": "Ruler",
            "role": "ADC",
            "salary": 6000.0,
            "status": "Benched"
        }
        # Lương gốc 6000.0 -> Thực lĩnh giảm một nửa còn 3000.0
        self.assertEqual(calculate_actual_pay(player_benched), 3000.0)

if __name__ == "__main__":
    unittest.main()