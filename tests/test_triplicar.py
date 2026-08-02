from demo_officina import triplicar


def test_triplicar_entero_positivo() -> None:
    """Verifica que triplicar regrese el triple de un entero positivo."""
    assert triplicar(2) == 6


def test_triplicar_cero() -> None:
    """Verifica que triplicar de cero sea cero."""
    assert triplicar(0) == 0


def test_triplicar_float_negativo() -> None:
    """Verifica que triplicar regrese el triple de un flotante negativo."""
    assert triplicar(-1.5) == -4.5
