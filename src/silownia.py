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

    def dodaj_klienta(self, klient: Klient) -> None:
        if klient in self.klienci:
            print(f"Klient {klient.imie} {klient.nazwisko} już istnieje.")
        else:
            self.klienci.append(klient)
            print(f"Dodano klienta: {klient.imie} {klient.nazwisko}")

    def dodaj_instruktora(self, instruktor: Instruktor) -> None:
        if instruktor in self.instruktorzy:
            print(f"Instruktor {instruktor.imie} {instruktor.nazwisko} już istnieje.")
        else:
            self.instruktorzy.append(instruktor)
            print(f"Dodano instruktora: {instruktor.imie} {instruktor.nazwisko}")

    def zaplanuj_zajecia(self, zajecia: Zajecia) -> None:
        if zajecia in self.zajecia:
            print(f"Zajęcia {zajecia.nazwa} - {zajecia.data} już istnieją.")
        else:
            self.__sprawdz_zaplanowane_zajecia(zajecia)
            self.zajecia.append(zajecia)
            print(f"Dodano zajęcia: {zajecia.nazwa} - {zajecia.data}")

    def __sprawdz_zaplanowane_zajecia(self, zajecia) -> None:
        godziny_rozpoczecia_zajec = [zajecia.data for zajecia in self.zajecia]
        if zajecia.data in godziny_rozpoczecia_zajec:
            raise ValueError("Zajecia nie mogą odbywać się w tym samym czasie")

    def wyswietl_czlonkow(self) -> None:
        ilosc_czlonkow = len(self.klienci)
        aktywni_czlonkowie = [f"{klient.imie} {klient.nazwisko}" for klient in self.klienci if klient.status == "aktywny"]
        ilosc_aktywnych_czlonkow = len(aktywni_czlonkowie)
        nieaktywni_czlonkowie = [f"{klient.imie} {klient.nazwisko}" for klient in self.klienci if klient.status == "nieaktywny"]
        ilosc_nieaktywnych_czlonkow = len(nieaktywni_czlonkowie)
        print(f"Siłownia {self.nazwa} posiada {ilosc_czlonkow} członków.")
        print(f"{ilosc_aktywnych_czlonkow} z {ilosc_czlonkow} posiada aktywny karnet.")
        print(f"{ilosc_nieaktywnych_czlonkow} z {ilosc_czlonkow} nie opłaciło swojego karnetu za ten miesiąc.")

    def wyswietl_instruktorow(self) -> None:
        ilosc_instruktorow = len(self.instruktorzy)
        lista_specjalizacji = []
        for insturktor in self.instruktorzy:
            lista_specjalizacji.extend(insturktor.specjalizacje)
        unikalne_specjalizacje = list(set(lista_specjalizacji))
        ilosc_unikalnych_specalizacji = len(unikalne_specjalizacje)
        print(f"Siłownia {self.nazwa} zatrudnia {ilosc_instruktorow}")
        print(f"Specjalizacje instruktorów dotyczą {ilosc_unikalnych_specalizacji} obszarów: {', '.join(unikalne_specjalizacje)}")
        print("Lista instruktorów:")
        for instruktor in self.instruktorzy:
            print(f"- {instruktor.imie} {instruktor.nazwisko}, specjalizacje: {', '.join(instruktor.specjalizacje)}")

    def wyswietl_zajecia(self) -> None:
        aktualny_czas = datetime.now()
        zrealizowane_zajecia = [zajecia for zajecia in self.zajecia if zajecia.data < aktualny_czas]
        ilosc_zrealizowanych_zajec = len(zrealizowane_zajecia)
        zaplanowane_zajecia = [zajecia for zajecia in self.zajecia if zajecia.data >= aktualny_czas]
        ilosc_zaplanowanych_zajec = len(zaplanowane_zajecia)
        print(f"Zajęcia w siłowni {self.nazwa}:")
        if zrealizowane_zajecia:
            print(f"Zrealizowano {ilosc_zrealizowanych_zajec} zajęć:")
            for zajecia in zrealizowane_zajecia:
                print(f"- {zajecia.nazwa} - {zajecia.data}")
        else:
            print("Brak zrealizowanych zajęć.")
        if zaplanowane_zajecia:
            print(f"Zaplanowano {ilosc_zaplanowanych_zajec} zajęć:")
            for zajecia in zaplanowane_zajecia:
                print(f"- {zajecia.nazwa} - {zajecia.data}")
        else:
            print("Brak zaplanowanych zajęć.")
