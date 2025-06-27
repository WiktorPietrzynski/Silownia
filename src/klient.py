from src.karnet import Karnet
from src.osoba import Osoba


class Klient(Osoba):
    ostatnie_id = 0

    def __init__(self, imie: str, nazwisko: str, data_urodzenia: str, email: str = None, telefon: str = None):
        self.id = Klient.ostatnie_id + 1
        Klient.ostatnie_id = self.id
        super().__init__(imie, nazwisko, data_urodzenia, email, telefon)
        self.status = "nieaktywny"
        self.karnet = None

    def dodaj_karnet(self, karnet: Karnet) -> None:
        if self.karnet is not None:
            print("Klient już posiada karnet. Proszę anulować obecny karnet przed dodaniem nowego.")
        else:
            self.status = "aktywny"
            self.karnet = karnet
            print(f"Karnet dla klienta {self.imie} {self.nazwisko} został dodany.")

    def przedluz_karnet(self, dlugosc: int) -> None:
        if self.karnet is None:
            print("Klient nie posiada aktywnego karnetu. Proszę najpierw dodać karnet.")
        else:
            self.karnet.przedluz_karnet(dlugosc)

    def anuluj_karnet(self, powod: str = None) -> None:
        if self.karnet is None:
            print("Klient nie posiada aktywnego karnetu do anulowania.")
        else:
            self.status = "nieaktywny"
            self.karnet.anuluj_karnet(powod)
            self.karnet = None
