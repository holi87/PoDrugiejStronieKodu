from biblioteka import zrob_parzysta
__author__ = "Grzegorz Holak"


def dzielenie(x, y):
    if y % 2 == 0:
        return x / y
    else:
        return x / zrob_parzysta(y)
