from src.models.klient import Klient
from src.models.instruktor import Instruktor
from src.utils import *


class Zajecia:
    def __init__(self, nazwa: str, data: str, czas_trwania: float):
        self.nazwa = nazwa
        self.data = sprawdz_format_daty(data)
        self.czas_trwania = czas_trwania
        self.opis = None
        self.uczestnicy = []
        self.instruktor = None
        self.limit_uczestnikow = 10

    def __str__(self):
        return f"{self.nazwa} - {self.data} ({self.czas_trwania} godz.)\n Opis: {self.opis}\n"

    def dodaj_uczestnika(self, klient: Klient):
        if len(self.uczestnicy) <= self.limit_uczestnikow:
            self.uczestnicy.append(klient)
        else:
            print(f"Nie można dodać uczestnika {klient.imie} {klient.nazwisko}. Limit uczestników został przekroczony.")

    def usun_uczestnika(self, klient: Klient):
        if klient in self.uczestnicy:
            self.uczestnicy.remove(klient)
        else:
            print(f"Uczestnik {klient.imie} {klient.nazwisko} nie jest zapisany na te zajęcia.")

    def dodaj_instruktora(self, instruktor: Instruktor):
        if self.instruktor is None:
            self.instruktor = instruktor
        else:
            print("Zajęcia już mają przypisanego instruktora.")

    def usun_instruktora(self, instruktor: Instruktor):
        if self.instruktor == instruktor:
            self.instruktor = None
        else:
            print("Ten instruktor nie jest przypisany do tych zajęć.")

    def ustaw_limit_uczestnikow(self, limit: int):
        if limit >= 0:
            self.limit_uczestnikow = limit
        else:
            print("Limit uczestników nie może być ujemny.")

    def zapelnienie(self):
        print(f"Zajęcia '{self.nazwa}' są wypełnione w {len(self.uczestnicy)}/{self.limit_uczestnikow} uczestników.")
        print("Wone miejsca:", self.limit_uczestnikow - len(self.uczestnicy))
