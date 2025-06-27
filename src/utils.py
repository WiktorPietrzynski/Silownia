import re
from datetime import datetime


def sprawdz_format_daty(data: str) -> str:
    """
    Sprawdza, czy podana data ma poprawny format 'YYYY-MM-DD'.

    Parameters
    ----------
    data : str
        Data do sprawdzenia.

    Returns
    -------
    str
        Zwraca datę, jeśli format jest poprawny.

    Raises
    ------
    ValueError
        Jeśli data nie jest w formacie 'YYYY-MM-DD'.
    """
    try:
        datetime.strptime(data, "%Y-%m-%d")
        return data
    except ValueError:
        raise ValueError(f"Niepoprawny format daty: {data}. Oczekiwany format to YYYY-MM-DD.")


def sprawdz_format_email(email: str) -> str:
    """
    Sprawdza, czy podany adres e-mail ma poprawny format.

    Parameters
    ----------
    email : str
        Adres e-mail do sprawdzenia.

    Returns
    -------
    str
        Zwraca e-mail, jeśli format jest poprawny.

    Raises
    ------
    ValueError
        Jeśli adres e-mail nie spełnia podstawowych wymagań składniowych.
    """
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return email
    else:
        raise ValueError(f"Niepoprawny format adresu e-mail: {email}.")


def sprawdz_format_telefonu(telefon: str) -> str:
    """
    Sprawdza, czy numer telefonu składa się z dokładnie 9 cyfr.

    Parameters
    ----------
    telefon : str
        Numer telefonu do sprawdzenia.

    Returns
    -------
    str
        Zwraca numer telefonu, jeśli format jest poprawny.

    Raises
    ------
    ValueError
        Jeśli numer telefonu nie zawiera dokładnie 9 cyfr.
    """
    if re.match(r"^\d{9}$", telefon):
        return telefon
    else:
        raise ValueError(f"Niepoprawny format numeru telefonu: {telefon}. Oczekiwany format to np. 123456789.")
