from datetime import datetime


class Klient:
    ostatnie_id = 0

    def __init__(self, imie: str, nazwisko: str, data_urodzenia: str, email: str = None, telefon: str = None):
        self.id = Klient.ostatnie_id + 1
        Klient.ostatnie_id = self.id
        self.imie = imie
        self.nazwisko = nazwisko
        self.data_urodzenia = data_urodzenia
        self.wiek = self.__ustal_wiek()
        self.email = email
        self.telefon = telefon
        self.status = "nieaktywny"
        self.karnet = None
        self.ulga = None

    def __ustal_wiek(self):
        data_urodzenia = datetime.strptime(self.data_urodzenia, "%Y-%m-%d")
        dzisiaj = datetime.now()
        return dzisiaj.year - data_urodzenia.year - ((dzisiaj.month, dzisiaj.day) < (data_urodzenia.month, data_urodzenia.day))

    def dodaj_karnet(self, karnet):
        pass

    def przedluz_karnet(self, dlugosc):
        pass

    def anuluj_karnet(self):
        pass

    def dodaj_ulge(self, ulga):
        pass

    def zmien_dane(self):
        pass
