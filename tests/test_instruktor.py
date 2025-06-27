import unittest
from unittest.mock import patch
from src.instruktor import Instruktor


class TestInstruktor(unittest.TestCase):
    @patch('src.osoba.sprawdz_format_daty', return_value="1985-06-15")
    @patch('src.osoba.sprawdz_format_email', return_value="instruktor@example.com")
    @patch('src.osoba.sprawdz_format_telefonu', return_value="123456789")
    def test_utworzenie_instruktora(self, mock_tel, mock_email, mock_data):
        instruktor = Instruktor("Anna", "Nowak", "1985-06-15", "instruktor@example.com", "123456789")
        self.assertEqual(instruktor.imie, "Anna")
        self.assertEqual(instruktor.nazwisko, "Nowak")
        self.assertEqual(instruktor.specjalizacje, [])
        self.assertGreater(instruktor.id, 0)

    @patch('src.osoba.sprawdz_format_daty', return_value="1985-06-15")
    @patch('src.osoba.sprawdz_format_email', return_value="instruktor@example.com")
    @patch('src.osoba.sprawdz_format_telefonu', return_value="123456789")
    def test_dodaj_specjalizacje(self, mock_tel, mock_email, mock_data):
        instruktor = Instruktor("Jan", "Kowalski", "1985-06-15", "instruktor@example.com", "123456789")
        instruktor.dodaj_specjalizacje("Joga")
        self.assertIn("Joga", instruktor.specjalizacje)

    @patch('src.osoba.sprawdz_format_daty', return_value="1985-06-15")
    @patch('src.osoba.sprawdz_format_email', return_value="instruktor@example.com")
    @patch('src.osoba.sprawdz_format_telefonu', return_value="123456789")
    def test_usun_specjalizacje(self, mock_tel, mock_email, mock_data):
        instruktor = Instruktor("Ewa", "Zielińska", "1985-06-15", "instruktor@example.com", "123456789")
        instruktor.dodaj_specjalizacje("Pilates")
        instruktor.usun_specjalizacje("Pilates")
        self.assertNotIn("Pilates", instruktor.specjalizacje)

    @patch('src.osoba.sprawdz_format_daty', return_value="1985-06-15")
    @patch('src.osoba.sprawdz_format_email', return_value="instruktor@example.com")
    @patch('src.osoba.sprawdz_format_telefonu', return_value="123456789")
    def test_str_repr(self, mock_tel, mock_email, mock_data):
        instruktor = Instruktor("Tomasz", "Lis", "1985-06-15", "instruktor@example.com", "123456789")
        instruktor.dodaj_specjalizacje("Crossfit")
        self.assertEqual(str(instruktor), "Tomasz Lis - Specjalizacje: Crossfit")


if __name__ == '__main__':
    unittest.main()
