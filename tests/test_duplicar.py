from demo_officina import duplicar


def test_duplicar_entero_positivo() -> None:
    """Verifica que duplicar regrese el doble de un entero positivo."""
    assert duplicar(3) == 6


def test_duplicar_cero() -> None:
    """Verifica que duplicar de cero sea cero."""
    assert duplicar(0) == 0


def test_duplicar_float_negativo() -> None:
    """Verifica que duplicar regrese el doble de un flotante negativo."""
    assert duplicar(-2.5) == -5.0
