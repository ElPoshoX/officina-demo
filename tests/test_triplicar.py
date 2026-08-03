"""Pruebas para triplicar."""

from demo_officina import triplicar


def test_triplicar_entero() -> None:
    """Verifica que triplicar regrese el triple de un entero."""
    assert triplicar(2) == 6


def test_triplicar_cero() -> None:
    """Verifica que triplicar de cero sea cero."""
    assert triplicar(0) == 0


def test_triplicar_float() -> None:
    """Verifica que triplicar regrese el triple de un flotante."""
    assert triplicar(1.5) == 4.5

