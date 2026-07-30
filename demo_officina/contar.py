"""Módulo contar para demo_officina."""


def contar_letras(texto: str) -> int:
    """contar_letras(texto) cuenta las letras del string.

    Regresa el número de caracteres para los cuales str.isalpha() es True.
    """
    return sum(1 for c in texto if c.isalpha())
