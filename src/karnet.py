from datetime import datetime, timedelta


class Karnet:
    """
    Reprezentuje karnet klienta siłowni, zawierający informacje o rodzaju, dacie rozpoczęcia, długości trwania, cenie i statusie.

    Attributes
    ----------
    rodzaj_karnetu : str
        Typ karnetu, np. "miesięczny", "roczny", "bezterminowy".
    data_rozpoczecia : str
        Data rozpoczęcia karnetu w formacie 'YYYY-MM-DD'.
    znizka : str or None
        Rodzaj zniżki, np. "studencka", "senior", "rodzinna", "wakacyjna".
    cena : float
        Cena karnetu po uwzględnieniu ewentualnej zniżki.
    dlugosc : int
        Długość trwania karnetu w miesiącach.
    data_zakonczenia : str
        Data zakończenia karnetu w formacie 'YYYY-MM-DD'.
    status : str
        Status karnetu, np. "aktywny" lub "nieaktywny".
    """

    def __init__(self, rodzaj_karnetu: str, data_rozpoczecia: str, znizka: str = None):
        """
        Inicjalizuje nowy karnet na podstawie rodzaju, daty rozpoczęcia i ewentualnej zniżki.

        Parameters
        ----------
        rodzaj_karnetu : str
            Rodzaj karnetu.
        data_rozpoczecia : str
            Data rozpoczęcia karnetu.
        znizka : str, optional
            Rodzaj zniżki, jeśli dotyczy.
        """
        self.rodzaj_karnetu = rodzaj_karnetu
        self.data_rozpoczecia = data_rozpoczecia
        self.znizka = znizka
        self.cena = self.__ustal_cene(rodzaj_karnetu)
        self.dlugosc = self.__ustal_dlugosc(rodzaj_karnetu)
        self.data_zakonczenia = self.__ustal_date_zakonczenia(data_rozpoczecia, self.dlugosc)
        self.status = "aktywny"

    def anuluj_karnet(self, powod: str = None) -> None:
        """
        Anuluje karnet i ustala datę zakończenia na ostatni dzień miesiąca rozpoczęcia.

        Parameters
        ----------
        powod : str, optional
            Powód anulowania karnetu.
        """
        rok = datetime.strptime(self.data_rozpoczecia, "%Y-%m-%d").year
        miesiac = datetime.strptime(self.data_rozpoczecia, "%Y-%m-%d").month
        if miesiac == 12:
            nastepny_miesiac = datetime(rok + 1, 1, 1)
        else:
            nastepny_miesiac = datetime(rok, miesiac + 1, 1)
        ostatni_dzien_miesiaca = nastepny_miesiac - timedelta(days=1)
        print("Karnet został anulowany. Data zakończenia karnetu:", ostatni_dzien_miesiaca.strftime("%Y-%m-%d"))
        if powod:
            print(f"Karnet anulowany z powodu: {powod}")
        else:
            print("Karnet anulowany bez podania powodu.")
        self.status = "nieaktywny"

    def przedluz_karnet(self, liczba_miesiecy: int) -> None:
        """
        Przedłuża karnet o podaną liczbę miesięcy.

        Parameters
        ----------
        liczba_miesiecy : int
            Liczba miesięcy, o którą należy przedłużyć karnet.

        Raises
        ------
        ValueError
            Jeśli liczba miesięcy jest niepoprawna lub karnet jest bezterminowy.
        """
        if liczba_miesiecy <= 0:
            raise ValueError("Liczba miesięcy do przedłużenia musi być większa niż 0.")
        if self.rodzaj_karnetu == "bezterminowy":
            raise ValueError("Karnet bezterminowy nie może być przedłużany.")
        data_rozpoczecia = datetime.strptime(self.data_zakonczenia, "%Y-%m-%d")
        nowa_data_zakonczenia = data_rozpoczecia + timedelta(days=30 * liczba_miesiecy)
        self.data_zakonczenia = nowa_data_zakonczenia.strftime("%Y-%m-%d")
        if liczba_miesiecy == 1:
            slowo = "miesiąc"
        elif liczba_miesiecy in [2, 3, 4]:
            slowo = "miesiące"
        else:
            slowo = "miesięcy"
        print(f"Karnet został przedłużony o {liczba_miesiecy} {slowo}. Nowa data zakończenia: {self.data_zakonczenia}")

    def odnow_karnetu(self):
        """
        Odnawia karnet, jeśli jego status to "nieaktywny".

        Raises
        ------
        ValueError
            Jeśli karnet jest już aktywny.
        """
        if self.status == "aktywny":
            raise ValueError("Karnet jest już aktywny. Nie można go odnowić.")
        self.status = "aktywny"
        print(f"Karnet został odnowiony. Data rozpoczęcia: {self.data_rozpoczecia}, Data zakończenia: {self.data_zakonczenia}")

    def __ustal_cene(self, rodzaj_karnetu: str) -> float:
        """
        Ustala cenę karnetu na podstawie rodzaju i ewentualnej zniżki.

        Parameters
        ----------
        rodzaj_karnetu : str
            Rodzaj karnetu.

        Returns
        -------
        float
            Cena końcowa karnetu.
        """
        ceny = {
            "miesięczny": 180.0,
            "polroczny": 150.0,
            "roczny": 130.0,
            "bezterminowy": 140.0
        }
        if rodzaj_karnetu in ceny:
            cena_karnetu = ceny[rodzaj_karnetu]
        else:
            raise ValueError(f"Nieznany rodzaj karnetu: {rodzaj_karnetu}. Cena ustawiona na 0.")
        znizki = {
            "studencka": 0.8,
            "senior": 0.9,
            "rodzinna": 0.85,
            "wakacyjna": 0.95
        }
        if self.znizka in znizki:
            cena_karnetu *= znizki[self.znizka]
        return cena_karnetu

    @staticmethod
    def __ustal_dlugosc(rodzaj_karnetu: str) -> int:
        """
        Ustala długość trwania karnetu w miesiącach.

        Parameters
        ----------
        rodzaj_karnetu : str
            Rodzaj karnetu.

        Returns
        -------
        int
            Liczba miesięcy trwania karnetu.
        """
        dlugosci = {
            "miesięczny": 1,
            "trzymiesięczny": 3,
            "roczny": 12
        }
        return dlugosci.get(rodzaj_karnetu, 0)

    @staticmethod
    def __ustal_cene_miesieczna(cena: float, dlugosc: int) -> float:
        """
        Oblicza cenę miesięczną karnetu.

        Parameters
        ----------
        cena : float
            Cena całkowita karnetu.
        dlugosc : int
            Długość trwania karnetu w miesiącach.

        Returns
        -------
        float
            Cena za jeden miesiąc.
        """
        return cena / dlugosc if dlugosc > 0 else 0.0

    @staticmethod
    def __ustal_date_zakonczenia(data_rozpoczecia: str, dlugosc: int) -> str:
        """
        Oblicza datę zakończenia karnetu na podstawie daty rozpoczęcia i długości.

        Parameters
        ----------
        data_rozpoczecia : str
            Data rozpoczęcia karnetu.
        dlugosc : int
            Długość trwania karnetu w miesiącach.

        Returns
        -------
        str
            Data zakończenia karnetu w formacie 'YYYY-MM-DD'.
        """
        data_rozpoczecia = datetime.strptime(data_rozpoczecia, "%Y-%m-%d")
        data_zakonczenia = data_rozpoczecia.replace(month=data_rozpoczecia.month + dlugosc)
        return data_zakonczenia.strftime("%Y-%m-%d")
