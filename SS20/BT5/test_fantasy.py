import unittest
from main import calc_actual_withdrawal

class TestFantasyLeagueLogic(unittest.TestCase):
    
    def test_valid_withdrawal_fee(self):
        """Test Case 1: Nhập vào 100 token hợp lệ -> Trả về 90.0 sau khi trừ 10% phí"""
        self.assertEqual(calc_actual_withdrawal(100), 90.0)
        self.assertEqual(calc_actual_withdrawal(500), 450.0)

    def test_negative_withdrawal_error(self):
        """Test Case 2: Nhập vào số âm hoặc số 0 -> Hệ thống phải sinh ra lỗi ValueError"""
        with self.assertRaises(ValueError):
            calc_actual_withdrawal(-50)
            
        with self.assertRaises(ValueError):
            calc_actual_withdrawal(0)

if __name__ == "__main__":
    unittest.main()