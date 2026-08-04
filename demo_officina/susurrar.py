"""Módulo susurrar para demo_officina."""


def susurrar(texto: str) -> str:
    """Regresa el texto en minúsculas."""
    return texto.lower()


def susurrar_dos_veces(texto: str) -> str:
    """Regresa el texto en minúsculas repetido dos veces."""
    return texto.lower() * 2


def contar_susurros(texto: str) -> int:
    """Cuenta ocurrencias no traslapadas e insensibles a mayúsculas de 'psst'."""
    return texto.lower().count("psst")
