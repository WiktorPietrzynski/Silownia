from src.klient import Klient
from src.instruktor import Instruktor
from src.utils import *


class Zajecia:
    """
    Reprezentuje zajęcia prowadzone w klubie fitness, z przypisanym instruktorem i listą uczestników.

    Attributes
    ----------
    ostatnie_id : int
        Statyczny licznik identyfikatorów zajęć.
    id : int
        Unikalny identyfikator zajęć.
    nazwa : str
        Nazwa zajęć (np. "Joga", "Crossfit").
    data : str
        Data zajęć w formacie 'YYYY-MM-DD'.
    czas_trwania : float
        Czas trwania zajęć w godzinach.
    opis : str or None
        Opcjonalny opis zajęć.
    uczestnicy : list of Klient
        Lista klientów zapisanych na zajęcia.
    instruktor : Instruktor or None
        Instruktor prowadzący zajęcia.
    limit_uczestnikow : int
        Maksymalna liczba uczestników, którzy mogą wziąć udział w zajęciach.
    """

    ostatnie_id = 0

    def __init__(self, nazwa: str, data: str, czas_trwania: float):
        """
        Inicjalizuje nowe zajęcia z podaną nazwą, datą i czasem trwania.

        Parameters
        ----------
        nazwa : str
            Nazwa zajęć.
        data : str
            Data zajęć w formacie 'YYYY-MM-DD'.
        czas_trwania : float
            Czas trwania zajęć w godzinach.
        """
        self.id = Zajecia.ostatnie_id + 1
        Zajecia.ostatnie_id = self.id
        self.nazwa = nazwa
        self.data = sprawdz_format_daty(data)
        self.czas_trwania = czas_trwania
        self.opis = None
        self.uczestnicy = []
        self.instruktor = None
        self.limit_uczestnikow = 10

    def __str__(self) -> str:
        """
        Zwraca tekstową reprezentację zajęć.

        Returns
        -------
        str
            Opis zajęć zawierający nazwę, datę, czas trwania i opis.
        """
        return f"{self.nazwa} - {self.data} ({self.czas_trwania} godz.)\n Opis: {self.opis}\n"

    def dodaj_uczestnika(self, klient: Klient) -> None:
        """
        Dodaje klienta do listy uczestników, jeśli nie został przekroczony limit.

        Parameters
        ----------
        klient : Klient
            Obiekt klienta do dodania.

        Returns
        -------
        None
        """
        if len(self.uczestnicy) <= self.limit_uczestnikow:
            self.uczestnicy.append(klient)
        else:
            print(f"Nie można dodać uczestnika {klient.imie} {klient.nazwisko}. Limit uczestników został przekroczony.")

    def usun_uczestnika(self, klient: Klient) -> None:
        """
        Usuwa klienta z listy uczestników, jeśli jest zapisany.

        Parameters
        ----------
        klient : Klient
            Obiekt klienta do usunięcia.

        Returns
        -------
        None
        """
        if klient in self.uczestnicy:
            self.uczestnicy.remove(klient)
        else:
            print(f"Uczestnik {klient.imie} {klient.nazwisko} nie jest zapisany na te zajęcia.")

    def dodaj_instruktora(self, instruktor: Instruktor) -> None:
        """
        Przypisuje instruktora do zajęć, jeśli żaden nie jest jeszcze przypisany.

        Parameters
        ----------
        instruktor : Instruktor
            Obiekt instruktora do przypisania.

        Returns
        -------
        None
        """
        if self.instruktor is None:
            self.instruktor = instruktor
        else:
            print("Zajęcia już mają przypisanego instruktora.")

    def usun_instruktora(self, instruktor: Instruktor) -> None:
        """
        Usuwa przypisanego instruktora, jeśli jest zgodny z aktualnym.

        Parameters
        ----------
        instruktor : Instruktor
            Obiekt instruktora do usunięcia.

        Returns
        -------
        None
        """
        if self.instruktor == instruktor:
            self.instruktor = None
        else:
            print("Ten instruktor nie jest przypisany do tych zajęć.")

    def ustaw_limit_uczestnikow(self, limit: int) -> None:
        """
        Ustawia nowy limit uczestników dla zajęć.

        Parameters
        ----------
        limit : int
            Nowy limit uczestników (musi być nieujemny).

        Returns
        -------
        None
        """
        if limit >= 0:
            self.limit_uczestnikow = limit
        else:
            print("Limit uczestników nie może być ujemny.")

    def zapelnienie(self) -> None:
        """
        Wyświetla informację o liczbie zapisanych uczestników i dostępnych miejscach.

        Returns
        -------
        None
        """
        print(f"Zajęcia '{self.nazwa}' są wypełnione w {len(self.uczestnicy)}/{self.limit_uczestnikow} uczestników.")
        print("Wolne miejsca:", self.limit_uczestnikow - len(self.uczestnicy))
