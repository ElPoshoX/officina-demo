from demo_officina import saludar


def test_saludar() -> None:
    """Verifica que saludar() regrese el saludo esperado."""
    assert saludar() == "hola officina"
