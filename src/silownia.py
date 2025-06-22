from src.klient import Klient
from src.instruktor import Instruktor
from src.zajecia import Zajecia
from datetime import datetime


class Silownia:
    def __init__(self, nazwa: str, lokalizacja: str):
        self.nazwa = nazwa
        self.lokalizacja = lokalizacja
        self.instruktorzy = []
        self.klienci = []
        self.zajecia = []

