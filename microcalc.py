#Copyright © 2026 Anas Boutaghroucht.All rights reserved.

"""
microcalc - Le moteur de calcul le plus léger du monde.
"""

def calculer(a, op, b):
    """
    Exécute un calcul simple.
    Usage: calculer(10, '*', 5) -> 50
    """
    # Dictionnaire des opérateurs autorisés pour la sécurité
    ops = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else "DivByZero",
        '**': lambda x, y: x ** y
    }
    
    try:
        # On convertit en float au cas où la machine envoie des strings
        num1, num2 = float(a), float(b)
        return ops[op](num1, num2)
    except (KeyError, ValueError, TypeError):
        return "Error"

