"""Pruebas para bostezar."""

from demo_officina import bostezar


def test_bostezar_texto() -> None:
    """Verifica que bostezar concatene '...' y convierta a minúsculas."""
    assert bostezar("Hola") == "hola..."


def test_bostezar_vacio() -> None:
    """Verifica que bostezar con cadena vacía regrese '...'."""
    assert bostezar("") == "..."
