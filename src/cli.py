from src.instruktor import Instruktor
from src.karnet import Karnet
from src.silownia import Silownia
from src.klient import Klient
from src.zajecia import Zajecia


def run_cli() -> None:
    print("Zarządzanie członkostwem na siłowni")
    nazwa_silowni = "Twoja Siłownia"
    lokalizacja_silowni = "Warszawa, ul. Przykładowa 1"
    silownia = Silownia(nazwa_silowni, lokalizacja_silowni)
    while True:
        print("\nMenu:")
        print("1. Zarządzaj klientami")
        print("2. Zarządzaj instruktorami")
        print("3. Zarządzaj zajęciami")
        print("4. Wyświetl członków siłowni")
        print("5. Wyświetl instruktorów siłowni")
        print("6. Wyświetl zajęcia siłowni")
        print("7. Wyjdź")
        choice = str(input("Wybierz opcję: "))
        if choice == "1":
            zarzadzanie_klientami(silownia)
        elif choice == "2":
            zarzadzanie_instruktorami(silownia)
        elif choice == "3":
            zarzadzanie_zajeciami(silownia)
        elif choice == "4":
            print("\nCzłonkowie siłowni:")
            if len(silownia.klienci) == 0:
                print("Brak klientów przypisanych do siłowni.")
            else:
                silownia.wyswietl_czlonkow()
        elif choice == "5":
            print("\nInstruktorzy siłowni:")
            if len(silownia.instruktorzy) == 0:
                print("Brak instruktorów przypisanych do siłowni.")
            else:
                silownia.wyswietl_instruktorow()
        elif choice == "6":
            print("\nZajęcia siłowni:")
            if len(silownia.zajecia) == 0:
                print("Brak zajęć przypisanych do siłowni.")
            else:
                silownia.wyswietl_zajecia()
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")


def zarzadzanie_klientami(silownia: Silownia) -> None:
    while True:
        print("\nZarządzanie klientami:")
        print("1. Dodaj klienta")
        print("3. Przypisz karnet klientowi")
        print("4. Przedluz karnet klientowi")
        print("5. Anuluj karnet klientowi")
        print("6. Zmien dane klienta")
        print("7. Wróć do menu głównego")
        sub_choice = str(input("Wybierz opcję: "))
        if sub_choice == "1":
            klient = dodawanie_klienta()
            silownia.dodaj_klienta(klient)
        elif sub_choice == "2":
            klient = wybor_klienta(silownia)
            przypisz_karnet(klient)
        elif sub_choice == "3":
            dlugosc_przedluzenia = int(input("Podaj liczbę miesięcy do przedłużenia: "))
            klient = wybor_klienta(silownia)
            klient.przedluz_karnet(dlugosc_przedluzenia)
        elif sub_choice == "4":
            klient = wybor_klienta(silownia)
            powod = str(input("Podaj powód anulowania karnetu (opcjonalnie): "))
            klient.anuluj_karnet(powod)
        elif sub_choice == "5":
            klient = wybor_klienta(silownia)
            klient.zmien_dane(*zmiana_danych())
        elif sub_choice == "6":
            print("Wracanie do menu głównego...")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")


def dodawanie_klienta() -> Klient:
    print("Dodawanie nowego klienta:")
    imie = str(input("Podaj imię klienta: "))
    nazwisko = str(input("Podaj nazwisko klienta: "))
    data_urodzenia = str(input("Podaj datę urodzenia klienta (YYYY-MM-DD): "))
    email = str(input("Podaj email klienta: "))
    telefon = str(input("Podaj telefon klienta: "))
    return Klient(imie, nazwisko, data_urodzenia, email, telefon)


def przypisz_karnet(klient) -> None:
    print("Wybierz rodzaj karnetu: miesięczny, półroczny, roczny lub bezterminowy.")
    rodzaj_karnetu = str(input("Podaj rodzaj karnetu: "))
    data_rozpoczecia = str(input("Podaj datę rozpoczęcia karnetu (YYYY-MM-DD): "))
    znizka = str(input("Podaj rodzaj ulgi (studencka, senior, rodzinna, wakacyjna) lub pozostaw puste: "))
    karnet = Karnet(rodzaj_karnetu, data_rozpoczecia, znizka)
    klient.dodaj_karnet(karnet)


def dodawanie_instruktora() -> Instruktor:
    imie = str(input("Podaj imię instruktora: "))
    nazwisko = str(input("Podaj nazwisko instruktora: "))
    specjalizacja = str(input("Podaj specjalizację instruktora: "))
    return Instruktor(imie, nazwisko, specjalizacja)


def dodawanie_zajec() -> Zajecia:
    nazwa_zajec = str(input("Podaj nazwę zajęć: "))
    data_zajec = str(input("Podaj datę zajęć (YYYY-MM-DD): "))
    czas_trwania = float(input("Podaj czas trwania zajęć (w minutach): "))
    zajecia = Zajecia(nazwa_zajec, data_zajec, czas_trwania)
    return zajecia


def wybor_klienta(silownia: Silownia) -> Klient:
    print("Wybierz klienta:")
    if len(silownia.klienci) == 0:
        print("Brak klientów przypisanych do silowni.")
        return dodawanie_klienta()
    for klient in silownia.klienci:
        print(f"{klient.id}. {klient.imie} {klient.nazwisko}")
    wybor = int(input("Podaj ID klienta: "))
    for klient in silownia.klienci:
        if klient.id == wybor:
            return klient
    return dodawanie_klienta()


def zarzadzanie_instruktorami(silownia: Silownia) -> None:
    while True:
        print("\nZarządzanie instruktorami:")
        print("1. Dodaj instruktora")
        print("2. Przypisz specjalizację instruktorowi")
        print("3. Usuń specjalizację instruktorowi")
        print("4. Zmien dane instruktora")
        print("5. Wróć do menu głównego")
        sub_choice = str(input("Wybierz opcję: "))
        if sub_choice == "1":
            instruktor = dodawanie_instruktora()
            silownia.dodaj_instruktora(instruktor)
        elif sub_choice == "2":
            instruktor = wybor_instruktora(silownia)
            specjalizacja = str(input("Podaj specjalizację do dodania: "))
            instruktor.dodaj_specjalizacje(specjalizacja)
        elif sub_choice == "3":
            instruktor = wybor_instruktora(silownia)
            specjalizacja = str(input("Podaj specjalizację do usunięcia: "))
            instruktor.usun_specjalizacje(specjalizacja)
        elif sub_choice == "4":
            instruktor = wybor_instruktora(silownia)
            instruktor.zmien_dane(*zmiana_danych())
        elif sub_choice == "5":
            print("Wracanie do menu głównego...")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")


def wybor_instruktora(silownia: Silownia) -> Instruktor:
    print("Wybierz instruktora:")
    if len(silownia.instruktorzy) == 0:
        print("Brak instruktorów przypisanych do siłowni.")
        return dodawanie_instruktora()
    for instruktor in silownia.instruktorzy:
        print(f"{instruktor.id}. {instruktor.imie} {instruktor.nazwisko}")
    wybor = int(input("Podaj ID instruktora: "))
    for instruktor in silownia.instruktorzy:
        if instruktor.id == wybor:
            return instruktor
    return dodawanie_instruktora()


def zmiana_danych() -> tuple:
    imie = str(input("Podaj nowe imię instruktora (lub pozostaw puste, aby nie zmieniać): "))
    nazwisko = str(input("Podaj nowe nazwisko instruktora (lub pozostaw puste, aby nie zmieniać): "))
    data_urodzenia = str(input("Podaj nową datę urodzenia instruktora (YYYY-MM-DD) (lub pozostaw puste, aby nie zmieniać): "))
    email = str(input("Podaj nowy email instruktora (opcjonalnie, lub pozostaw puste, aby nie zmieniać): "))
    telefon = str(input("Podaj nowy telefon instruktora (opcjonalnie, lub pozostaw puste, aby nie zmieniać): "))
    return imie, nazwisko, data_urodzenia, email, telefon


def zarzadzanie_zajeciami(silownia: Silownia) -> None:
    while True:
        print("\nZarządzanie zajęciami:")
        print("1. Dodaj zajęcia")
        print("2. Przypisz instruktora do zajęć")
        print("3. Usuń instruktora z zajęć")
        print("4. Dodaj uczestnika do zajęć")
        print("5. Usuń uczestnika z zajęć")
        print("6. Ustaw limit uczestników zajęć")
        print("7. Wyświetl zapełnienie zajęć")
        print("8. Wróć do menu głównego")
        sub_choice = str(input("Wybierz opcję: "))
        if sub_choice == "1":
            zajecia = dodawanie_zajec()
            silownia.zaplanuj_zajecia(zajecia)
        elif sub_choice == "2":
            zajecia = wybor_zajec(silownia)
            instruktor = wybor_instruktora(silownia)
            zajecia.dodaj_instruktora(instruktor)
        elif sub_choice == "3":
            zajecia = wybor_zajec(silownia)
            instruktor = wybor_instruktora(silownia)
            zajecia.usun_instruktora(instruktor)
        elif sub_choice == "4":
            zajecia = wybor_zajec(silownia)
            klient = wybor_klienta(silownia)
            zajecia.dodaj_uczestnika(klient)
        elif sub_choice == "5":
            zajecia = wybor_zajec(silownia)
            klient = wybor_klienta(silownia)
            zajecia.usun_uczestnika(klient)
        elif sub_choice == "6":
            zajecia = wybor_zajec(silownia)
            limit = int(input("Podaj nowy limit uczestników: "))
            zajecia.ustaw_limit_uczestnikow(limit)
        elif sub_choice == "7":
            zajecia = wybor_zajec(silownia)
            zajecia.zapelnienie()
        elif sub_choice == "8":
            print("Wracanie do menu głównego...")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")


def wybor_zajec(silownia: Silownia) -> Zajecia:
    print("Wybierz zajęcia:")
    if len(silownia.zajecia) == 0:
        print("Brak zajęć przypisanych do siłowni.")
        return dodawanie_zajec()
    for zajecia in silownia.zajecia:
        print(f"{zajecia.id}. {zajecia.nazwa} - {zajecia.data}")
    wybor = int(input("Podaj ID zajęć: "))
    for zajecia in silownia.zajecia:
        if zajecia.id == wybor:
            return zajecia
    return dodawanie_zajec()
