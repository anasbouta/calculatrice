# Copyright © 2026 Anas Boutaghroucht. All rights reserved.

"""
microcalc - Le moteur de calcul le plus léger du monde.
"""

import math

_ops = {
    # ── Arithmétique de base ──────────────────────────────
    '+':    lambda x, y: x + y,
    '-':    lambda x, y: x - y,
    '*':    lambda x, y: x * y,
    '/':    lambda x, y: x / y          if y != 0  else "DivByZero",
    '//':   lambda x, y: x // y         if y != 0  else "DivByZero",
    '%':    lambda x, y: x % y          if y != 0  else "DivByZero",
    '**':   lambda x, y: x ** y,

    # ── Maths avancées (y ignoré) ─────────────────────────
    'sqrt': lambda x, _: math.sqrt(x)   if x >= 0  else "NegativeSqrt",
    'log':  lambda x, _: math.log(x)    if x > 0   else "LogError",
    'log2': lambda x, _: math.log2(x)   if x > 0   else "LogError",
    'log10':lambda x, _: math.log10(x)  if x > 0   else "LogError",
    'abs':  lambda x, _: abs(x),
    'ceil': lambda x, _: math.ceil(x),
    'floor':lambda x, _: math.floor(x),

    # ── Trigonométrie (x en radians) ─────────────────────
    'sin':  lambda x, _: math.sin(x),
    'cos':  lambda x, _: math.cos(x),
    'tan':  lambda x, _: math.tan(x),
}


def calculer(a, op: str, b=0):
    """
    Exécute un calcul simple.

    Opérateurs binaires  : calculer(10, '+', 5)   → 15.0
    Opérateurs unaires   : calculer(9, 'sqrt')     → 3.0
                           calculer(-4, 'abs')     → 4.0
                           calculer(0.5, 'sin')    → 0.479...

    Opérateurs disponibles :
        Arithmétique : + - * / // % **
        Maths        : sqrt log log2 log10 abs ceil floor
        Trigo        : sin cos tan
    """
    if op not in _ops:
        return "UnknownOp"
    try:
        return _ops[op](float(a), float(b))
    except (ValueError, TypeError):
        return "Error"


def ops_disponibles() -> list[str]:
    """Retourne la liste de tous les opérateurs supportés."""
    return list(_ops.keys())
