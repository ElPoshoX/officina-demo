"""Paquete demo para cards de officina."""

from demo_officina.saludar import saludar as saludar

__version__ = "0.1.0"


def version() -> str:
    """Regresa la version del paquete."""
    return __version__


def saludar() -> str:
    """Regresa un saludo a officina."""
    return "hola officina"
