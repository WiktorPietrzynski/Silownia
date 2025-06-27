from src.karnet import Karnet
from src.osoba import Osoba


class Klient(Osoba):
    """
    Reprezentuje klienta siłowni, dziedziczącego po klasie `Osoba`.

    Attributes
    ----------
    ostatnie_id : int
        Licznik statyczny służący do nadawania unikalnych identyfikatorów klientom.
    id : int
        Unikalny identyfikator klienta.
    status : str
        Status klienta, np. "aktywny" lub "nieaktywny".
    karnet : Karnet or None
        Obiekt klasy `Karnet` przypisany do klienta lub `None`, jeśli klient nie posiada karnetu.
    """
    ostatnie_id = 0

    def __init__(self, imie: str, nazwisko: str, data_urodzenia: str, email: str = None, telefon: str = None):
        """
        Inicjalizuje nowego klienta z podstawowymi danymi osobowymi.

        Parameters
        ----------
        imie : str
            Imię klienta.
        nazwisko : str
            Nazwisko klienta.
        data_urodzenia : str
            Data urodzenia klienta w formacie 'YYYY-MM-DD'.
        email : str, optional
            Adres e-mail klienta.
        telefon : str, optional
            Numer telefonu klienta.
        """
        self.id = Klient.ostatnie_id + 1
        Klient.ostatnie_id = self.id
        super().__init__(imie, nazwisko, data_urodzenia, email, telefon)
        self.status = "nieaktywny"
        self.karnet = None

    def dodaj_karnet(self, karnet: Karnet) -> None:
        """
        Dodaje klientowi nowy karnet, jeśli nie posiada już aktywnego.

        Parameters
        ----------
        karnet : Karnet
            Obiekt karnetu, który ma zostać przypisany klientowi.

        Returns
        -------
        None
        """
        if self.karnet is not None:
            print("Klient już posiada karnet. Proszę anulować obecny karnet przed dodaniem nowego.")
        else:
            self.status = "aktywny"
            self.karnet = karnet
            print(f"Karnet dla klienta {self.imie} {self.nazwisko} został dodany.")

    def przedluz_karnet(self, dlugosc: int) -> None:
        """
        Przedłuża aktualny karnet klienta o podaną liczbę dni.

        Parameters
        ----------
        dlugosc : int
            Liczba dni, o którą należy przedłużyć karnet.

        Returns
        -------
        None
        """
        if self.karnet is None:
            print("Klient nie posiada aktywnego karnetu. Proszę najpierw dodać karnet.")
        else:
            self.karnet.przedluz_karnet(dlugosc)

    def anuluj_karnet(self, powod: str = None) -> None:
        """
        Anuluje aktualny karnet klienta i ustawia jego status na "nieaktywny".

        Parameters
        ----------
        powod : str, optional
            Powód anulowania karnetu.

        Returns
        -------
        None
        """
        if self.karnet is None:
            print("Klient nie posiada aktywnego karnetu do anulowania.")
        else:
            self.status = "nieaktywny"
            self.karnet.anuluj_karnet(powod)
            self.karnet = None
