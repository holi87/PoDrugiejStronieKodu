import unittest
import modul


class TestyModul(unittest.TestCase):
    def test_czy_dzielenie_4_przez_2_da_float(self):
        self.assertTrue(isinstance(modul.dzielenie(4, 2), float))

    def test_czy_dzielenie_12_przez_4_da_3(self):
        self.assertEqual(3, modul.dzielenie(12, 4))

if __name__ == '__main__':
    unittest.main()
