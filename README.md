# Diagrammes de Constellation QAM avec Ajustements pour \( p = 3 \)

Ce projet Python génère des diagrammes de constellations QAM (Quadrature Amplitude Modulation) avec des ajustements spécifiques pour différentes puissances, notamment \( p = 3 \). Le programme calcule les dimensions de la grille, applique des exclusions symétriques, et trace le diagramme résultant. Ce README fournit une explication détaillée de la structure du projet, des formules utilisées, et de la manière de lire les diagrammes.

---

## Aperçu du Projet

### Diagramme QAM pour \( p = 3 \)
![Diagramme QAM \( p = 3 \)](qam%20p%20%3D%203%20plot.jpg)

- **Points bleus** : Symboles valides utilisés pour la modulation.
- **Points rouges** : Symboles exclus selon les règles définies.

### Exemple de Sortie du Terminal
![Sortie Terminal](terminal%20output.jpg))

Le terminal affiche les dimensions de la grille et les exclusions pour chaque puissance.

---

## Fonctionnalités

1. **Calcul dynamique des dimensions de la grille** : Les dimensions (lignes et colonnes) sont calculées automatiquement en fonction de la puissance \( p \).
2. **Gestion des puissances impaires** : Le script applique des ajustements spéciaux pour les puissances impaires comme \( p = 3, 5, 7, 9 \).
3. **Exclusions symétriques** : Certaines points sont exclus de manière symétrique pour respecter les caractéristiques de la modulation QAM.
4. **Visualisation claire des constellations** : Le diagramme distingue les symboles valides (en bleu) et exclus (en rouge).

---

## Structure du Projet

- **`script_qam.py`** : Contient les fonctions principales pour le calcul des dimensions, la gestion des exclusions, et le tracé des diagrammes.
- **`qam_p=3_plot.jpg`** : Exemple de diagramme pour \( p = 3 \).
- **`terminal_output.jpg`** : Exemple de sortie du terminal avec les résultats calculés.

---

## Explications des Formules

### Fonction `calculer_lignes_colonnes(p)`

Cette fonction calcule les dimensions de la grille (lignes et colonnes) et le nombre d'exclusions \( soustraction \) pour une puissance \( p \). Les calculs dépendent de la parité de \( p \) :

1. **Puissance paire** :
   \[
   \text{lignes} = \text{colonnes} = 2^{p / 2}, \quad \text{soustraction} = 0
   \]

2. **Puissance impaire** :
   \[
   \text{lignes} = \text{colonnes} = 2^{(p // 2) + 1}, \quad \text{soustraction} = 2^{p - 3}
   \]

   Des ajustements supplémentaires sont faits pour \( p = 3, 5, 7, 9 \).

### Fonction `plot_qam_constellation(lignes, colonnes, soustraction, p)`

1. **Grille des points** :
   - Une grille de points est générée en utilisant \( X \) et \( Y \) avec les dimensions calculées.
   - Les exclusions sont appliquées symétriquement à travers les quatre quadrants.

2. **Exclusions symétriques** :
   - Les exclusions sont réparties uniformément dans un quadrant puis reproduites dans les autres quadrants pour préserver la symétrie.

3. **Tracé des points** :
   - Les points valides sont tracés en bleu et les points exclus en rouge.
   - Les axes et la grille sont ajoutés pour une meilleure lisibilité.

---

## Instructions d'Utilisation

### Prérequis

- Python 3.x
- Bibliothèques nécessaires : `matplotlib`, `numpy`

### Instructions

1. Clonez ce dépôt ou téléchargez les fichiers source.
2. Installez les dépendances nécessaires via pip :
   ```bash
   pip install matplotlib numpy
   Exécutez le script principal :

python script_qam.py

Cela affichera les résultats calculés pour chaque puissance et générera les diagrammes correspondants.

### Comment Lire un Diagramme QAM

## Axes :

# L'axe horizontal représente la composante en phase (In-Phase, I).

# L'axe vertical représente la composante quadrature (Quadrature, Q).

# Points bleus : Les symboles disponibles pour la transmission.

# Points rouges : Les symboles exclus pour maintenir la symétrie ou optimiser la modulation.

# Grille : La structure sous-jacente de la constellation.


Ce diagramme met en évidence les symboles valides et exclus sur une grille 4x4.

### Auteur

Ce script a été conçu pour explorer les constellations QAM et leurs ajustements spécifiques. Si vous avez des questions ou des suggestions, n'hésitez pas à ouvrir une issue ou à soumettre une pull request.
