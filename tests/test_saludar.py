from demo_officina import saludar


def test_saludar() -> None:
    assert saludar() == "hola officina"

