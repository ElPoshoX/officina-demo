from demo_officina import contar_susurros


def test_contar_susurros_mixed_case() -> None:
    """Verifica que contar_susurros cuente variantes mixtas de 'psst'."""
    assert contar_susurros("Psst, PSST, psst") == 3
