"""Tests para la función invertir."""

from demo_officina import invertir


def test_invertir_palabra() -> None:
    assert invertir("hola") == "aloh"


def test_invertir_vacio() -> None:
    assert invertir("") == ""


def test_invertir_unicode() -> None:
    assert invertir("café") == "éfac"


def test_invertir_un_caracter() -> None:
    assert invertir("x") == "x"
