import unittest
from unittest.mock import MagicMock
from datetime import datetime, timedelta
from src.silownia import Silownia
from src.klient import Klient
from src.instruktor import Instruktor
from src.zajecia import Zajecia


class TestSilownia(unittest.TestCase):

    def setUp(self):
        self.silownia = Silownia("FitZone", "Poznań")

    def test_dodaj_klienta(self):
        klient = MagicMock(spec=Klient)
        klient.imie = "Jan"
        klient.nazwisko = "Kowalski"
        self.silownia.dodaj_klienta(klient)
        self.assertIn(klient, self.silownia.klienci)

    def test_dodaj_instruktora(self):
        instruktor = MagicMock(spec=Instruktor)
        instruktor.imie = "Anna"
        instruktor.nazwisko = "Nowak"
        instruktor.specjalizacje = ["Joga"]
        self.silownia.dodaj_instruktora(instruktor)
        self.assertIn(instruktor, self.silownia.instruktorzy)

    def test_zaplanuj_zajecia(self):
        zajecia = MagicMock(spec=Zajecia)
        zajecia.nazwa = "Pilates"
        zajecia.data = datetime.now() + timedelta(days=1)
        self.silownia.zaplanuj_zajecia(zajecia)
        self.assertIn(zajecia, self.silownia.zajecia)

    def test_zaplanuj_zajecia_konflikt(self):
        zajecia1 = MagicMock(spec=Zajecia)
        zajecia1.nazwa = "Joga"
        zajecia1.data = datetime(2025, 7, 1, 10, 0)

        zajecia2 = MagicMock(spec=Zajecia)
        zajecia2.nazwa = "Crossfit"
        zajecia2.data = datetime(2025, 7, 1, 10, 0)

        self.silownia.zajecia.append(zajecia1)
        with self.assertRaises(ValueError):
            self.silownia.zaplanuj_zajecia(zajecia2)

    def test_wyswietl_czlonkow(self):
        klient1 = MagicMock(spec=Klient)
        klient1.imie = "Jan"
        klient1.nazwisko = "Kowalski"
        klient1.status = "aktywny"

        klient2 = MagicMock(spec=Klient)
        klient2.imie = "Ewa"
        klient2.nazwisko = "Nowak"
        klient2.status = "nieaktywny"

        self.silownia.klienci.extend([klient1, klient2])
        self.silownia.wyswietl_czlonkow()

    def test_wyswietl_instruktorow(self):
        instruktor = MagicMock(spec=Instruktor)
        instruktor.imie = "Anna"
        instruktor.nazwisko = "Nowak"
        instruktor.specjalizacje = ["Joga", "Pilates"]
        self.silownia.instruktorzy.append(instruktor)
        self.silownia.wyswietl_instruktorow()

    def test_wyswietl_zajecia(self):
        zajecia1 = MagicMock(spec=Zajecia)
        zajecia1.nazwa = "Joga"
        zajecia1.data = datetime.now() - timedelta(days=1)

        zajecia2 = MagicMock(spec=Zajecia)
        zajecia2.nazwa = "Crossfit"
        zajecia2.data = datetime.now() + timedelta(days=1)

        self.silownia.zajecia.extend([zajecia1, zajecia2])
        self.silownia.wyswietl_zajecia()


if __name__ == '__main__':
    unittest.main()
