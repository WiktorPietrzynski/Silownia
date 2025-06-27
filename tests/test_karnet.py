from src.karnet import Karnet
import unittest
from datetime import datetime, timedelta


class TestKarnet(unittest.TestCase):
    def test_utworzenie_karnetu(self):
        k = Karnet("miesięczny", "2025-06-01", "studencka")
        self.assertEqual(k.rodzaj_karnetu, "miesięczny")
        self.assertEqual(k.data_rozpoczecia, "2025-06-01")
        self.assertAlmostEqual(k.cena, 180.0 * 0.8)
        self.assertEqual(k.dlugosc, 1)
        self.assertEqual(k.status, "aktywny")

    def test_anulowanie_karnetu(self):
        k = Karnet("miesięczny", "2025-06-01")
        k.anuluj_karnet("przeprowadzka")
        self.assertEqual(k.status, "nieaktywny")

    def test_przedluzenie_karnetu(self):
        k = Karnet("miesięczny", "2025-06-01")
        stara_data = k.data_zakonczenia
        k.przedluz_karnet(2)
        nowa_data = datetime.strptime(stara_data, "%Y-%m-%d") + timedelta(days=60)
        self.assertEqual(k.data_zakonczenia, nowa_data.strftime("%Y-%m-%d"))

    def test_przedluzenie_karnetu_o_0_miesiecy(self):
        k = Karnet("miesięczny", "2025-06-01")
        with self.assertRaises(ValueError):
            k.przedluz_karnet(0)

    def test_przedluzenie_karnetu_bezterminowego(self):
        k = Karnet("bezterminowy", "2025-06-01")
        with self.assertRaises(ValueError):
            k.przedluz_karnet(1)

    def test_odnowienie_karnetu(self):
        k = Karnet("miesięczny", "2025-06-01")
        k.anuluj_karnet()
        k.odnow_karnetu()
        self.assertEqual(k.status, "aktywny")

    def test_odnowienie_aktywnego_karnetu(self):
        k = Karnet("miesięczny", "2025-06-01")
        with self.assertRaises(ValueError):
            k.odnow_karnetu()

    def test_nieznany_rodzaj_karnetu(self):
        with self.assertRaises(ValueError):
            Karnet("nieznany", "2025-06-01")


if __name__ == '__main__':
    unittest.main()
