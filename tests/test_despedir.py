from demo_officina import despedir


def test_despedir() -> None:
    """Verifica que despedir() regrese la despedida esperada."""
    assert despedir() == "adios officina"
