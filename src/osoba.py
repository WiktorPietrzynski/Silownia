from datetime import datetime
from src.utils import *


class Osoba:
    def __init__(self, imie: str, nazwisko: str, data_urodzenia: str, email: str, telefon: str):
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__data_urodzenia = sprawdz_format_daty(data_urodzenia)
        self.__wiek = self.__ustal_wiek()
        self.__email = sprawdz_format_email(email)
        self.__telefon = sprawdz_format_telefonu(telefon)

    def zmien_dane(self, imie: str = None, nazwisko: str = None, data_urodzenia: str = None, email: str = None, telefon: str = None) -> str:
        if imie:
            self.__imie = imie
        if nazwisko:
            self.__nazwisko = nazwisko
        if data_urodzenia:
            self.__data_urodzenia = sprawdz_format_daty(data_urodzenia)
            self.__wiek = self.__ustal_wiek()
        if email:
            self.__email = email
        if telefon:
            self.__telefon = telefon
        return f"Dane {self.__imie} {self.__nazwisko} zostały zaktualizowane."

    @property
    def imie(self) -> str:
        return self.__imie

    @property
    def nazwisko(self) -> str:
        return self.__nazwisko

    def wyswietl_dane(self) -> None:
        print(f"Imię: {self.__imie}, Nazwisko: {self.__nazwisko}, Data urodzenia: {self.__data_urodzenia}, Email: {self.__email}, Telefon: {self.__telefon}")

    def __ustal_wiek(self) -> int:
        data_urodzenia = datetime.strptime(self.__data_urodzenia, "%Y-%m-%d")
        dzisiaj = datetime.now()
        return int(dzisiaj.year - data_urodzenia.year - ((dzisiaj.month, dzisiaj.day) < (data_urodzenia.month, data_urodzenia.day)))
