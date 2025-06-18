class Instruktor:
    def __init__(self, imie: str, nazwisko: str, data_urodzenia: str, email: str = None, telefon: str = None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.data_urodzenia = data_urodzenia
        self.email = email
        self.telefon = telefon
        self.specjalizacje = []
        print(f"Instruktor {self.imie} {self.nazwisko} został dodany.")

    def __str__(self):
        return f"{self.imie} {self.nazwisko} ({self.data_urodzenia}) - Specjalizacje: {', '.join(self.specjalizacje) if self.specjalizacje else 'Brak'}"

    def zmien_dane(self, imie: str = None, nazwisko: str = None, data_urodzenia: str = None, email: str = None, telefon: str = None):
        if imie:
            self.imie = imie
        if nazwisko:
            self.nazwisko = nazwisko
        if data_urodzenia:
            self.data_urodzenia = data_urodzenia
        if email:
            self.email = email
        if telefon:
            self.telefon = telefon
        print(f"Dane instruktora {self.imie} {self.nazwisko} zostały zaktualizowane.")

    def dodaj_specjalizacje(self, specjalizacja: str):
        if specjalizacja not in self.specjalizacje:
            self.specjalizacje.append(specjalizacja)
            print(f"Specjalizacja '{specjalizacja}' została dodana dla instruktora {self.imie} {self.nazwisko}.")
        else:
            print(f"Specjalizacja '{specjalizacja}' już istnieje dla instruktora {self.imie} {self.nazwisko}.")

    def usun_specjalizacje(self, specjalizacja: str):
        if specjalizacja in self.specjalizacje:
            self.specjalizacje.remove(specjalizacja)
            print(f"Specjalizacja '{specjalizacja}' została usunięta dla instruktora {self.imie} {self.nazwisko}.")
        else:
            print(f"Specjalizacja '{specjalizacja}' nie istnieje dla instruktora {self.imie} {self.nazwisko}.")