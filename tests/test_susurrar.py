from demo_officina import susurrar


def test_susurrar() -> None:
    """Verifica que susurrar convierta el texto a minúsculas."""
    assert susurrar("HOLA OFFICINA") == "hola officina"
    assert susurrar("PyThOn") == "python"
    assert susurrar("") == ""

