from demo_officina import susurrar_dos_veces


def test_susurrar_dos_veces_mayusculas() -> None:
    """Verifica que susurrar_dos_veces repita el texto en minúsculas."""
    assert susurrar_dos_veces("HOLA OFFICINA") == "hola officinahola officina"


def test_susurrar_dos_veces_vacio() -> None:
    """Verifica que susurrar_dos_veces con cadena vacía regrese vacío."""
    assert susurrar_dos_veces("") == ""


def test_susurrar_dos_veces_mixto() -> None:
    """Verifica que susurrar_dos_veces convierta texto mixto y lo repita."""
    assert susurrar_dos_veces("HoLa OfFiCiNa") == "hola officinahola officina"
