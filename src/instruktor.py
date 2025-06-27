from src.osoba import Osoba


class Instruktor(Osoba):
    ostatnie_id = 0

    def __init__(self, imie: str, nazwisko: str, data_urodzenia: str, email: str = None, telefon: str = None):
        self.id = Instruktor.ostatnie_id + 1
        Instruktor.ostatnie_id = self.id
        super().__init__(imie, nazwisko, data_urodzenia, email, telefon)
        self.specjalizacje = []
        print(f"Instruktor {self.imie} {self.nazwisko} został dodany.")

    def __str__(self) -> str:
        return f"{self.imie} {self.nazwisko} - Specjalizacje: {', '.join(self.specjalizacje) if self.specjalizacje else 'Brak'}"

    def dodaj_specjalizacje(self, specjalizacja: str) -> None:
        if specjalizacja not in self.specjalizacje:
            self.specjalizacje.append(specjalizacja)
            print(f"Specjalizacja '{specjalizacja}' została dodana dla instruktora {self.imie} {self.nazwisko}.")
        else:
            print(f"Specjalizacja '{specjalizacja}' już istnieje dla instruktora {self.imie} {self.nazwisko}.")

    def usun_specjalizacje(self, specjalizacja: str) -> None:
        if specjalizacja in self.specjalizacje:
            self.specjalizacje.remove(specjalizacja)
            print(f"Specjalizacja '{specjalizacja}' została usunięta dla instruktora {self.imie} {self.nazwisko}.")
        else:
            print(f"Specjalizacja '{specjalizacja}' nie istnieje dla instruktora {self.imie} {self.nazwisko}.")
