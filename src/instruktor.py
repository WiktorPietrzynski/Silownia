from src.osoba import Osoba


class Instruktor(Osoba):
    """
    Reprezentuje instruktora siłowni, dziedziczącego po klasie `Osoba`.

    Attributes
    ----------
    ostatnie_id : int
        Statyczny licznik identyfikatorów przypisywanych instruktorom.
    id : int
        Unikalny identyfikator instruktora.
    specjalizacje : list of str
        Lista specjalizacji przypisanych do instruktora, np. "fitness", "crossfit", "yoga".
    """

    ostatnie_id = 0

    def __init__(self, imie: str, nazwisko: str, data_urodzenia: str, email: str = None, telefon: str = None):
        """
        Inicjalizuje nowego instruktora z danymi osobowymi i pustą listą specjalizacji.

        Parameters
        ----------
        imie : str
            Imię instruktora.
        nazwisko : str
            Nazwisko instruktora.
        data_urodzenia : str
            Data urodzenia w formacie 'YYYY-MM-DD'.
        email : str, optional
            Adres e-mail instruktora.
        telefon : str, optional
            Numer telefonu instruktora.
        """
        self.id = Instruktor.ostatnie_id + 1
        Instruktor.ostatnie_id = self.id
        super().__init__(imie, nazwisko, data_urodzenia, email, telefon)
        self.specjalizacje = []
        print(f"Instruktor {self.imie} {self.nazwisko} został dodany.")

    def __str__(self) -> str:
        """
        Zwraca reprezentację tekstową instruktora wraz z jego specjalizacjami.

        Returns
        -------
        str
            Tekst zawierający imię, nazwisko i listę specjalizacji.
        """
        return f"{self.imie} {self.nazwisko} - Specjalizacje: {', '.join(self.specjalizacje) if self.specjalizacje else 'Brak'}"

    def dodaj_specjalizacje(self, specjalizacja: str) -> None:
        """
        Dodaje nową specjalizację do listy specjalizacji instruktora, jeśli jeszcze jej nie ma.

        Parameters
        ----------
        specjalizacja : str
            Nazwa specjalizacji do dodania.

        Returns
        -------
        None
        """
        if specjalizacja not in self.specjalizacje:
            self.specjalizacje.append(specjalizacja)
            print(f"Specjalizacja '{specjalizacja}' została dodana dla instruktora {self.imie} {self.nazwisko}.")
        else:
            print(f"Specjalizacja '{specjalizacja}' już istnieje dla instruktora {self.imie} {self.nazwisko}.")

    def usun_specjalizacje(self, specjalizacja: str) -> None:
        """
        Usuwa specjalizację z listy specjalizacji instruktora, jeśli istnieje.

        Parameters
        ----------
        specjalizacja : str
            Nazwa specjalizacji do usunięcia.

        Returns
        -------
        None
        """
        if specjalizacja in self.specjalizacje:
            self.specjalizacje.remove(specjalizacja)
            print(f"Specjalizacja '{specjalizacja}' została usunięta dla instruktora {self.imie} {self.nazwisko}.")
        else:
            print(f"Specjalizacja '{specjalizacja}' nie istnieje dla instruktora {self.imie} {self.nazwisko}.")
