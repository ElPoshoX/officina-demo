"""Módulo contar_susurros para demo_officina."""

import re


def contar_susurros(texto: str) -> int:
    """Cuenta la cantidad de veces que aparece la palabra 'psst' en el texto."""
    return len(re.findall(r"\bpsst\b", texto, flags=re.IGNORECASE))
