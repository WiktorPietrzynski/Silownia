from datetime import datetime
from src.utils import *


class Osoba:
    """
    Reprezentuje osobę z podstawowymi danymi osobowymi i metodami do ich zarządzania.

    Attributes
    ----------
    __imie : str
        Imię osoby.
    __nazwisko : str
        Nazwisko osoby.
    __data_urodzenia : str
        Data urodzenia w formacie 'YYYY-MM-DD'.
    __wiek : int
        Wiek osoby wyliczany na podstawie daty urodzenia.
    __email : str
        Adres e-mail osoby, sprawdzany pod względem poprawności formatu.
    __telefon : str
        Numer telefonu osoby, sprawdzany pod względem poprawności formatu.
    """

    def __init__(self, imie: str, nazwisko: str, data_urodzenia: str, email: str, telefon: str):
        """
        Inicjalizuje nową osobę z podanymi danymi osobowymi.

        Parameters
        ----------
        imie : str
            Imię osoby.
        nazwisko : str
            Nazwisko osoby.
        data_urodzenia : str
            Data urodzenia w formacie 'YYYY-MM-DD'.
        email : str
            Adres e-mail osoby.
        telefon : str
            Numer telefonu osoby.
        """
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__data_urodzenia = sprawdz_format_daty(data_urodzenia)
        self.__wiek = self.__ustal_wiek()
        self.__email = sprawdz_format_email(email)
        self.__telefon = sprawdz_format_telefonu(telefon)

    def zmien_dane(self, imie: str = None, nazwisko: str = None, data_urodzenia: str = None, email: str = None, telefon: str = None) -> str:
        """
        Aktualizuje dane osobowe osoby.

        Parameters
        ----------
        imie : str, optional
            Nowe imię.
        nazwisko : str, optional
            Nowe nazwisko.
        data_urodzenia : str, optional
            Nowa data urodzenia.
        email : str, optional
            Nowy adres e-mail.
        telefon : str, optional
            Nowy numer telefonu.

        Returns
        -------
        str
            Komunikat potwierdzający aktualizację danych.
        """
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
        """
        Zwraca imię osoby.

        Returns
        -------
        str
            Imię osoby.
        """
        return self.__imie

    @property
    def nazwisko(self) -> str:
        """
        Zwraca nazwisko osoby.

        Returns
        -------
        str
            Nazwisko osoby.
        """
        return self.__nazwisko

    def wyswietl_dane(self) -> None:
        """
        Wyświetla dane osobowe osoby w formacie tekstowym.

        Returns
        -------
        None
        """
        print(f"Imię: {self.__imie}, Nazwisko: {self.__nazwisko}, Data urodzenia: {self.__data_urodzenia}, Email: {self.__email}, Telefon: {self.__telefon}")

    def __ustal_wiek(self) -> int:
        """
        Oblicza wiek osoby na podstawie daty urodzenia.

        Returns
        -------
        int
            Wiek osoby.
        """
        data_urodzenia = datetime.strptime(self.__data_urodzenia, "%Y-%m-%d")
        dzisiaj = datetime.now()
        return int(dzisiaj.year - data_urodzenia.year - ((dzisiaj.month, dzisiaj.day) < (data_urodzenia.month, data_urodzenia.day)))
