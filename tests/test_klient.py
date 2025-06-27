import unittest
from unittest.mock import patch, MagicMock
from src.klient import Klient
from src.karnet import Karnet


class TestKlient(unittest.TestCase):
    @patch('src.osoba.sprawdz_format_daty', return_value="1990-01-01")
    @patch('src.osoba.sprawdz_format_email', return_value="test@example.com")
    @patch('src.osoba.sprawdz_format_telefonu', return_value="123456789")
    def test_utworzenie_klienta(self, mock_tel, mock_email, mock_data):
        klient = Klient("Jan", "Kowalski", "1990-01-01", "test@example.com", "123456789")
        self.assertEqual(klient.imie, "Jan")
        self.assertEqual(klient.nazwisko, "Kowalski")
        self.assertEqual(klient.status, "nieaktywny")
        self.assertIsNone(klient.karnet)
        self.assertGreater(klient.id, 0)

    @patch('src.osoba.sprawdz_format_daty', return_value="1990-01-01")
    @patch('src.osoba.sprawdz_format_email', return_value="test@example.com")
    @patch('src.osoba.sprawdz_format_telefonu', return_value="123456789")
    def test_dodaj_karnet(self, mock_tel, mock_email, mock_data):
        klient = Klient("Anna", "Nowak", "1990-01-01", "test@example.com", "123456789")
        karnet_mock = MagicMock(spec=Karnet)
        klient.dodaj_karnet(karnet_mock)
        self.assertEqual(klient.karnet, karnet_mock)
        self.assertEqual(klient.status, "aktywny")

    @patch('src.osoba.sprawdz_format_daty', return_value="1990-01-01")
    @patch('src.osoba.sprawdz_format_email', return_value="test@example.com")
    @patch('src.osoba.sprawdz_format_telefonu', return_value="123456789")
    def test_dodaj_karnet_gdy_juz_istnieje(self, mock_tel, mock_email, mock_data):
        klient = Klient("Anna", "Nowak", "1990-01-01", "test@example.com", "123456789")
        karnet_mock = MagicMock(spec=Karnet)
        klient.karnet = karnet_mock
        with self.assertLogs(level='INFO') as log:
            klient.dodaj_karnet(karnet_mock)
        self.assertEqual(klient.karnet, karnet_mock)

    @patch('src.osoba.sprawdz_format_daty', return_value="1990-01-01")
    @patch('src.osoba.sprawdz_format_email', return_value="test@example.com")
    @patch('src.osoba.sprawdz_format_telefonu', return_value="123456789")
    def test_przedluz_karnet(self, mock_tel, mock_email, mock_data):
        klient = Klient("Ewa", "Zielińska", "1990-01-01", "test@example.com", "123456789")
        karnet_mock = MagicMock(spec=Karnet)
        klient.karnet = karnet_mock
        klient.przedluz_karnet(2)
        karnet_mock.przedluz_karnet.assert_called_once_with(2)

    @patch('src.osoba.sprawdz_format_daty', return_value="1990-01-01")
    @patch('src.osoba.sprawdz_format_email', return_value="test@example.com")
    @patch('src.osoba.sprawdz_format_telefonu', return_value="123456789")
    def test_anuluj_karnet(self, mock_tel, mock_email, mock_data):
        klient = Klient("Tomasz", "Lis", "1990-01-01", "test@example.com", "123456789")
        karnet_mock = MagicMock(spec=Karnet)
        klient.karnet = karnet_mock
        klient.anuluj_karnet("rezygnacja")
        karnet_mock.anuluj_karnet.assert_called_once_with("rezygnacja")
        self.assertEqual(klient.status, "nieaktywny")
        self.assertIsNone(klient.karnet)


if __name__ == '__main__':
    unittest.main()
