import re


def sprawdz_format_daty(data: str) -> str:
    from datetime import datetime
    try:
        datetime.strptime(data, "%Y-%m-%d")
        return data
    except ValueError:
        raise ValueError(f"Niepoprawny format daty: {data}. Oczekiwany format to YYYY-MM-DD.")


def sprawdz_format_email(email: str) -> str:
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return email
    else:
        raise ValueError(f"Niepoprawny format adresu e-mail: {email}.")


def sprawdz_format_telefonu(telefon: str) -> str:
    if re.match(r"^\d{9}$", telefon):
        return telefon
    else:
        raise ValueError(f"Niepoprawny format numeru telefonu: {telefon}. Oczekiwany format to np. 123456789.")
