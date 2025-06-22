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
