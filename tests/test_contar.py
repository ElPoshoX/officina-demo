from demo_officina import contar_letras


def test_contar_letras() -> None:
    """Verifica que contar_letras cuente correctamente las letras."""
    assert contar_letras("hola") == 4
    assert contar_letras("hola mundo") == 9
    assert contar_letras("123 !") == 0
    assert contar_letras("") == 0
    assert contar_letras("Áéx") == 3
