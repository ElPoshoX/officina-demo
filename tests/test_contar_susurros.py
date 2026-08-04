from demo_officina import contar_susurros


def test_contar_susurros_mixed_case() -> None:
    """Verifica que contar_susurros cuente 'psst' sin importar mayúsculas."""
    assert contar_susurros("Psst, psst! PSST") == 3
