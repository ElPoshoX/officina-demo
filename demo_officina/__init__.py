"""Paquete demo para cards de officina."""

from demo_officina.saludar import saludar as saludar
from demo_officina.despedir import despedir as despedir
from demo_officina.duplicar import duplicar as duplicar
from demo_officina.susurrar import susurrar as susurrar
from demo_officina.susurrar import susurrar_dos_veces as susurrar_dos_veces
from demo_officina.triplicar import triplicar as triplicar
from demo_officina.susurrar import contar_susurros as contar_susurros

__version__ = "0.1.0"


def version() -> str:
    """Regresa la version del paquete."""
    return __version__
