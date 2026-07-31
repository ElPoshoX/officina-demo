"""Tests para la función susurrar."""


from demo_officina import susurrar


def test_susurrar_convierte_a_minusculas() -> None:
    assert susurrar("HOLA") == "hola"


def test_susurrar_preserva_texto_mezclado() -> None:
    assert susurrar("Mundo") == "mundo"


def test_susurrar_preserva_numeros_y_espacios() -> None:
    assert susurrar("") == ""
    assert susurrar("Ya Existen 123") == "ya existen 123"
