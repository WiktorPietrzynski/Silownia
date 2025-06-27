import unittest
from unittest.mock import patch, MagicMock
from src.zajecia import Zajecia
from src.klient import Klient
from src.instruktor import Instruktor


class TestZajecia(unittest.TestCase):
    @patch('src.zajecia.sprawdz_format_daty', return_value="2025-07-01")
    def test_utworzenie_zajec(self, mock_data):
        zajecia = Zajecia("Joga", "2025-07-01", 1.5)
        self.assertEqual(zajecia.nazwa, "Joga")
        self.assertEqual(zajecia.data, "2025-07-01")
        self.assertEqual(zajecia.czas_trwania, 1.5)
        self.assertEqual(zajecia.limit_uczestnikow, 10)
        self.assertEqual(zajecia.uczestnicy, [])
        self.assertIsNone(zajecia.instruktor)

    @patch('src.zajecia.sprawdz_format_daty', return_value="2025-07-01")
    def test_dodaj_i_usun_uczestnika(self, mock_data):
        zajecia = Zajecia("Pilates", "2025-07-01", 1.0)
        klient = MagicMock(spec=Klient)
        zajecia.dodaj_uczestnika(klient)
        self.assertIn(klient, zajecia.uczestnicy)
        zajecia.usun_uczestnika(klient)
        self.assertNotIn(klient, zajecia.uczestnicy)

    @patch('src.zajecia.sprawdz_format_daty', return_value="2025-07-01")
    def test_limit_uczestnikow(self, mock_data):
        zajecia = Zajecia("Crossfit", "2025-07-01", 1.0)
        zajecia.ustaw_limit_uczestnikow(5)
        self.assertEqual(zajecia.limit_uczestnikow, 5)

    @patch('src.zajecia.sprawdz_format_daty', return_value="2025-07-01")
    def test_dodaj_instruktora(self, mock_data):
        zajecia = Zajecia("Stretching", "2025-07-01", 1.0)
        instruktor = MagicMock(spec=Instruktor)
        zajecia.dodaj_instruktora(instruktor)
        self.assertEqual(zajecia.instruktor, instruktor)

    @patch('src.zajecia.sprawdz_format_daty', return_value="2025-07-01")
    def test_usun_instruktora(self, mock_data):
        zajecia = Zajecia("Zumba", "2025-07-01", 1.0)
        instruktor = MagicMock(spec=Instruktor)
        zajecia.dodaj_instruktora(instruktor)
        zajecia.usun_instruktora(instruktor)
        self.assertIsNone(zajecia.instruktor)

    @patch('src.zajecia.sprawdz_format_daty', return_value="2025-07-01")
    def test_str_repr(self, mock_data):
        zajecia = Zajecia("Aerobik", "2025-07-01", 1.0)
        zajecia.opis = "Zajęcia dla każdego"
        self.assertIn("Aerobik - 2025-07-01 (1.0 godz.)", str(zajecia))
        self.assertIn("Opis: Zajęcia dla każdego", str(zajecia))


if __name__ == '__main__':
    unittest.main()
