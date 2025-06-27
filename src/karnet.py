from datetime import datetime, timedelta


class Karnet:

    def __init__(self, rodzaj_karnetu: str, data_rozpoczecia: str, znizka: str = None):
        self.rodzaj_karnetu = rodzaj_karnetu
        self.data_rozpoczecia = data_rozpoczecia
        self.znizka = znizka
        self.cena = self.__ustal_cene(rodzaj_karnetu)
        self.dlugosc = self.__ustal_dlugosc(rodzaj_karnetu)
        self.data_zakonczenia = self.__ustal_date_zakonczenia(data_rozpoczecia, self.dlugosc)
        self.status = "aktywny"

    def anuluj_karnet(self, powod: str = None) -> None:
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
        if liczba_miesiecy <= 0:
            raise ValueError("Liczba miesięcy do przedłużenia musi być większa niż 0.")
        if self.rodzaj_karnetu == "bezterminowy":
            raise ValueError("Karnet bezterminowy nie może być przedłużany.")
        data_rozpoczecia = datetime.strptime(self.data_zakonczenia, "%Y-%m-%d")
        nowa_data_zakonczenia = data_rozpoczecia + timedelta(days=30 * liczba_miesiecy)
        self.data_zakonczenia = nowa_data_zakonczenia.strftime("%Y-%m-%d")
        if liczba_miesiecy == 1:
            slowo = "miesiąc"
        elif liczba_miesiecy == 2 or liczba_miesiecy == 3 or liczba_miesiecy == 4:
            slowo = "miesiące"
        else:
            slowo = "miesięcy"
        print(f"Karnet został przedłużony o {liczba_miesiecy} {slowo}. Nowa data zakończenia: {self.data_zakonczenia}")

    def odnow_karnetu(self):
        if self.status == "aktywny":
            raise ValueError("Karnet jest już aktywny. Nie można go odnowić.")
        self.status = "aktywny"
        print(f"Karnet został odnowiony. Data rozpoczęcia: {self.data_rozpoczecia}, Data zakończenia: {self.data_zakonczenia}")

    def __ustal_cene(self, rodzaj_karnetu: str) -> float:
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
        dlugosci = {
            "miesięczny": 1,
            "trzymiesięczny": 3,
            "roczny": 12
        }
        return dlugosci.get(rodzaj_karnetu, 0)

    @staticmethod
    def __ustal_cene_miesieczna(cena: float, dlugosc: int) -> float:
        return cena / dlugosc if dlugosc > 0 else 0.0

    @staticmethod
    def __ustal_date_zakonczenia(data_rozpoczecia: str, dlugosc: int) -> str:
        data_rozpoczecia = datetime.strptime(data_rozpoczecia, "%Y-%m-%d")
        data_zakonczenia = data_rozpoczecia.replace(month=data_rozpoczecia.month + dlugosc)
        return data_zakonczenia.strftime("%Y-%m-%d")
