"""Módulo susurrar para demo_officina."""


def susurrar(texto: str) -> str:
    """Regresa el texto en minúsculas."""
    return texto.lower()


def susurrar_dos_veces(texto: str) -> str:
    """Regresa el texto en minúsculas repetido dos veces."""
    return texto.lower() * 2


def contar_susurros(texto: str) -> int:
    """Cuenta las ocurrencias no traslapadas de 'psst' sin distinguir mayúsculas."""
    return texto.lower().count("psst")
