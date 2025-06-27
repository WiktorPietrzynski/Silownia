# Czlonkostwo: Zarządzanie członkowstem siłowni

## Spis treści
1. [Opis projektu](#opis-projektu)
2. [Wymagania](#wymagania)
3. [Funkcjonalności](#funkcjonalności)
4. [Instalacja](#instalacja)
5. [Autorzy](#autorzy)


## Opis projektu

Aplikacja służy do uproszczonego zarządzania członkostwem w siłowni. Umożliwia dodawanie klientów, instruktorów, karnetów oraz zajęć.

## Wymagania
Python 3.11 lub nowszy

## Funkcjonalności

Projekt składa się z kilku podstawowych klas:

1. **Klient** - Dane klienta, informacje o jego członkostwie
- dodawanie klienta
- przypisywanie karnetu do klienta
2. **Instruktor** - Dane instruktora, informacje o specjalizacjach
- dodawanie instruktora
- dodawanie specjalizacji do instruktora
3. **Karnet** - Informacje o karnetach, ich typach i ważności
- dodawanie karnetu
- anulowanie karnetu
- przedłużanie karnetu
4. **Zajęcia** - Informacje o zajęciach
- dodawanie zajęć
- przypisywanie klientów do zajęć
- odwoływanie klientów z zajęć
- przypisywanie instruktora do zajęć
- sprawdzanie dostępności miejsc na zajęcia
- sprawdzanie listy klientów zapisanych na zajęcia
5. **Siłownia** - Zarządzanie siłownią, w tym dodawanie klientów, instruktorów i zajęć
- wyświetlanie listy klientów
- wyświetlanie listy instruktorów
- wyświetlanie listy zajęć
- dodawanie instruktorów do siłowni
- dodawanie klientów do siłowni
- dodawanie zajęć do siłowni
6. **Osoba** - Klasa bazowa dla klienta i instruktora, zawiera wspólne atrybuty takie jak imię, nazwisko, numer telefonu
- zmiana danych osobowych
- sprawdzanie danych osobowych

## Instalacja
Aby uruchomić projek nie jest wymagana żadna dodatkowa instalacja. Wystarczy sklonować repozytorium i uruchomić plik `main.py`

## Autorzy
- Wiktor Pietrzyński (@WiktorPietrzynski) - 125134
- Łukasz Dębski (@L-debski) - 126759
