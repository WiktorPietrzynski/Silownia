from src.klient import Klient
from src.instruktor import Instruktor
from src.zajecia import Zajecia
from datetime import datetime


class Silownia:
    def __init__(self, nazwa: str, lokalizacja: str):
        self.nazwa = nazwa
        self.lokalizacja = lokalizacja
        self.instruktorzy = []
        self.klienci = []
        self.zajecia = []

    def dodaj_klienta(self, klient: Klient):
        if klient in self.klienci:
            print(f"Klient {klient.imie} {klient.nazwisko} już istnieje.")
        else:
            self.klienci.append(klient)
            print(f"Dodano klienta: {klient.imie} {klient.nazwisko}")

    def dodaj_instruktora(self, instruktor: Instruktor):
        if instruktor in self.instuktorzy:
            print(f"Instruktor {instruktor.imie} {instruktor.nazwisko} już istnieje.")
        else:
            self.instuktorzy.append(instruktor)
            print(f"Dodano instruktora: {instruktor.imie} {instruktor.nazwisko}")

    def zaplanuj_zajecia(self, zajecia: Zajecia):
        if zajecia in self.zajecia:
            print(f"Zajęcia {zajecia.nazwa} - {zajecia.data} już istnieją.")
        else:
            self.__sprawdz_zaplanowane_zajecia(zajecia)
            self.zajecia.append(zajecia)
            print(f"Dodano zajęcia: {zajecia.nazwa} - {zajecia.data}")

    def __sprawdz_zaplanowane_zajecia(self, zajecia):
        godziny_rozpoczecia_zajec = [zajecia.data for zajecia in self.zajecia]
        if zajecia.data in godziny_rozpoczecia_zajec:
            raise ValueError("Zajecia nie mogą odbywać się w tym samym czasie")

