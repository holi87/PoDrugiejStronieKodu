from biblioteka import zrob_parzysta
__author__ = "Grzegorz Holak"


def dzielenie(dzielna, dzielnik):
    if not dzielnik % 2 == 0:
        dzielnik = zrob_parzysta(dzielnik)
    elif dzielnik == 0:
        return dzielna
    return dzielna / dzielnik

