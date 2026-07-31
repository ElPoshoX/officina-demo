"""Módulo susurrar para demo_officina."""


def susurrar(texto: str) -> str:
    """Regresa el texto convertido a minúsculas."""
    if not isinstance(texto, str):
        raise TypeError("susurrar espera una cadena de texto")
    return texto.lower()
