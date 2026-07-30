from demo_officina import contar_letras


def test_contar_letras_hola123() -> None:
    """Verifica que contar_letras('Hola123') == 4."""
    assert contar_letras("Hola123") == 4


def test_contar_letras_con_acentos_y_signos() -> None:
    """Verifica que contar_letras('¡Hola, mundo!') == 9."""
    assert contar_letras("¡Hola, mundo!") == 9


def test_contar_letras_vacio() -> None:
    """Verifica que contar_letras('') == 0."""
    assert contar_letras("") == 0


def test_contar_letras_letras_acentuadas_mayusculas() -> None:
    """Verifica que contar_letras('ABCñÁÉÍÓÚ') == 8."""
    assert contar_letras("ABCñÁÉÍÓÚ") == 8

