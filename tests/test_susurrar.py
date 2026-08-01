from demo_officina import susurrar


def test_susurrar_mayusculas() -> None:
    """Verifica que susurrar convierta mayúsculas a minúsculas."""
    assert susurrar("HOLA OFFICINA") == "hola officina"


def test_susurrar_minusculas() -> None:
    assert susurrar("hola officina") == "hola officina"


def test_susurrar_mixto() -> None:
    """Verifica que susurrar convierta texto mixto a minúsculas."""
    assert susurrar("HoLa OfFiCiNa") == "hola officina"
