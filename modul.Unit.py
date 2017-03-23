import unittest
import modul


class TestyModul(unittest.TestCase):
    def test_czy_dzielenie_4_przez_2_da_float(self):
        self.assertTrue(isinstance(modul.dzielenie(4,2), float))

if __name__ == '__main__':
    unittest.main()
