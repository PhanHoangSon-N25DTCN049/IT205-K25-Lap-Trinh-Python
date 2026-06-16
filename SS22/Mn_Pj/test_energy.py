import unittest
from main import calculate_energy_financials

class TestEnergyFinancials(unittest.TestCase):

    def test_under_discount_threshold(self):
        mock_devices = [
            {'id': 'T01', 'location': 'Zone A', 'old_index': 0, 'new_index': 10000, 'status': 'Normal'},
            {'id': 'T02', 'location': 'Zone B', 'old_index': 0, 'new_index': 20000, 'status': 'Normal'}
        ]
        total_cons, discount, final_cost = calculate_energy_financials(mock_devices)
        self.assertEqual(total_cons, 30000)
        self.assertEqual(discount, 0)
        self.assertEqual(final_cost, 30000 * 3000)

    def test_at_and_over_discount_threshold(self):
        mock_devices = [
            {'id': 'T01', 'location': 'Zone A', 'old_index': 0, 'new_index': 30000, 'status': 'Normal'},
            {'id': 'T02', 'location': 'Zone B', 'old_index': 0, 'new_index': 30000, 'status': 'Normal'}
        ]
        total_cons, discount, final_cost = calculate_energy_financials(mock_devices)
        self.assertEqual(total_cons, 60000)
        self.assertEqual(discount, 3)
        expected_cost = int((60000 * 3000) * 0.97)
        self.assertEqual(final_cost, expected_cost)

if __name__ == '__main__':
    unittest.main()