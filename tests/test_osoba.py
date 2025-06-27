import unittest
from unittest.mock import patch
from datetime import datetime
from src.osoba import Osoba


class TestOsoba(unittest.TestCase):

    @patch('src.osoba.sprawdz_format_daty', return_value="2000-01-01")
    @patch('src.osoba.sprawdz_format_email', return_value="jan@example.com")
    @patch('src.osoba.sprawdz_format_telefonu', return_value="123456789")
    def test_utworzenie_osoby(self, mock_tel, mock_email, mock_data):
        osoba = Osoba("Jan", "Kowalski", "2000-01-01", "jan@example.com", "123456789")
        self.assertEqual(osoba.imie, "Jan")
        self.assertEqual(osoba.nazwisko, "Kowalski")

    @patch('src.osoba.sprawdz_format_daty', return_value="1990-05-15")
    @patch('src.osoba.sprawdz_format_email', return_value="anna@example.com")
    @patch('src.osoba.sprawdz_format_telefonu', return_value="987654321")
    def test_zmien_dane(self, mock_tel, mock_email, mock_data):
        osoba = Osoba("Anna", "Nowak", "1990-05-15", "anna@example.com", "987654321")
        wynik = osoba.zmien_dane(imie="Ewa", nazwisko="Kowalska")
        self.assertEqual(osoba.imie, "Ewa")
        self.assertEqual(osoba.nazwisko, "Kowalska")
        self.assertIn("Dane Ewa Kowalska zostały zaktualizowane.", wynik)

    @patch('src.osoba.sprawdz_format_daty', return_value="2000-01-01")
    @patch('src.osoba.sprawdz_format_email', return_value="test@example.com")
    @patch('src.osoba.sprawdz_format_telefonu', return_value="123456789")
    def test_wiek_osoby(self, mock_tel, mock_email, mock_data):
        osoba = Osoba("Jan", "Kowalski", "2000-01-01", "test@example.com", "123456789")
        dzisiaj = datetime.now()
        wiek_oczekiwany = dzisiaj.year - 2000 - ((dzisiaj.month, dzisiaj.day) < (1, 1))
        self.assertEqual(osoba._Osoba__wiek, wiek_oczekiwany)


if __name__ == '__main__':
    unittest.main()
