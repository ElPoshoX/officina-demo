from demo_officina import contar_susurros


def test_contar_susurros() -> None:
    """Verifica el conteo de 'psst' sin importar mayúsculas."""
    assert contar_susurros("") == 0
    assert contar_susurros("psst") == 1
    assert contar_susurros("PSsT") == 1
    assert contar_susurros("pssst") == 0
    assert contar_susurros("PsSt, psst!") == 2
    assert contar_susurros("PsSt PSsT") == 2
