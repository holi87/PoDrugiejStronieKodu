import unittest
import modul


class TestyModul(unittest.TestCase):
    def test_czy_dzielenie_4_przez_2_da_float(self):
        self.assertTrue(isinstance(modul.dzielenie(4, 2), float))

    def test_czy_dzielenie_12_przez_4_da_3(self):
        self.assertEqual(3, modul.dzielenie(12, 4))

    def test_czy_dzielenie_12_przez_3_da_3(self):  # dzielnik zwieksza sie o 1, czyli de fato 12/4 = 3
        self.assertEqual(3, modul.dzielenie(12, 3))

    def test_czy_dzielenie_20_przez_0_da_20(self):  # dzielnik = 0, wiec zwraca dzielna
        self.assertEqual(20, modul.dzielenie(20, 0))

if __name__ == '__main__':
    unittest.main()
