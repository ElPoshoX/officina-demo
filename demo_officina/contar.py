"""Módulo contar para demo_officina."""


def contar_letras(texto: str) -> int:
    """Cuenta cuántos caracteres del string son letras.

    Usa str.isalpha(), por lo que incluye letras acentuadas, ñ,
    mayúsculas/minúsculas, y excluye dígitos, espacios, signos de
    puntuación y emojis.
    """
    return sum(1 for caracter in texto if caracter.isalpha())

