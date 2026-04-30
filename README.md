
---

# 🧮 Mathlight (Microcalc) V0.2.1

![License](https://img.shields.io/badge/license-Custom-red)
![Python](https://img.shields.io/badge/Language-Python-blue)
![PyPI](https://img.shields.io/badge/PIP-Mathlight-green)

**Mathlight** est le moteur de calcul le plus léger du monde. Conçu pour être atomique et ultra-rapide, ce paquet Python permet d'intégrer des fonctions de calcul de base dans n'importe quel projet sans aucune dépendance externe.

## 🌟 Fonctionnalités Clés

* **Légèreté Absolue :** Zéro dépendance, du pur Python pour une exécution instantanée.
* **Sécurité Intégrée :** Utilisation d'un dictionnaire d'opérateurs autorisés pour éviter l'exécution de code malveillant.
* **Polyvalence :** Supporte l'addition, la soustraction, la multiplication, la division et les puissances.
* **Gestion d'Erreur :** Protection native contre la division par zéro et les entrées invalides.

## 🛠️ Spécifications Techniques

* **Moteur :** Basé sur le module `microcalc.py`.
* **Compatibilité :** Fonctionne avec Python 3.11 et versions supérieures.
* **Distribution :** Automatisée via GitHub Actions pour garantir des versions stables sur PyPI.

## 🚀 Installation rapide

1.  **Via PIP (Recommandé) :**
    ```bash
    pip install Mathlight
    ```
2.  **Usage dans votre code :**
    ```python
    from microcalc import calculer

    resultat = calculer(10, '*', 5)
    print(resultat) # Affiche 50.0
    ```
##MAJ

1.Maintenent avec math avancé!

 ```python
    from microcalc import calculer

# Opérations de base
print(calculer(10, '+', 5))     # 15.0
print(calculer(10, '/', 0))     # "DivByZero"

# Maths avancées
print(calculer(9, 'sqrt'))      # 3.0
print(calculer(4.7, 'floor'))   # 4.0

# Trigonométrie
print(calculer(0, 'sin'))       # 0.0
  ```

## ⚖️ Licence

Ce projet est distribué sous une licence personnalisée.
* **Attribution :** Crédit obligatoire envers l'auteur original (Anas Boutaghroucht).
* **Pas de Modification :** Le logiciel doit être utilisé dans sa forme originale.
*Copyright (c) 2026 Anas Boutaghroucht*.

---
