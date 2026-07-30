"""Paquete demo para cards de officina."""

from demo_officina.saludar import saludar as saludar
from demo_officina.despedir import despedir as despedir


def invertir(texto: str) -> str:
    """Regresa la cadena de texto invertida."""
    return texto[::-1]


__version__ = "0.1.0"


def version() -> str:
    """Regresa la version del paquete."""
    return __version__
