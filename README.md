Diagrammes de Constellation QAM avec Ajustements pour 

Ce projet Python génère des diagrammes de constellations QAM (Quadrature Amplitude Modulation) avec des ajustements spécifiques pour différentes puissances, notamment . Le programme calcule les dimensions de la grille, applique des exclusions symétriques, et trace le diagramme résultant. Ce README fournit une explication détaillée de la structure du projet, des formules utilisées, et de la manière de lire les diagrammes.

Fonctionnalités

Calcul dynamique des dimensions de la grille : Les dimensions (lignes et colonnes) sont calculées automatiquement en fonction de la puissance .

Gestion des puissances impaires : Le script applique des ajustements spéciaux pour les puissances impaires comme .

Exclusions symétriques : Certaines points sont exclus de manière symétrique pour respecter les caractéristiques de la modulation QAM.

Visualisation claire des constellations : Le diagramme distingue les symboles valides (en bleu) et exclus (en rouge).

Structure du Projet

script_qam.py : Contient les fonctions principales pour le calcul des dimensions, la gestion des exclusions, et le tracé des diagrammes.

qam_p=3_plot.jpg : Exemple de diagramme pour .

terminal_output.jpg : Exemple de sortie du terminal avec les résultats calculés.

Explications des Formules

Fonction calculer_lignes_colonnes(p)

Cette fonction calcule les dimensions de la grille (lignes et colonnes) et le nombre d'exclusions  pour une puissance . Les calculs dépendent de la parité de  :

Puissance paire :

Puissance impaire :

Des ajustements supplémentaires sont faits pour .

Fonction plot_qam_constellation(lignes, colonnes, soustraction, p)

Grille des points :

Une grille de points est générée en utilisant  et  avec les dimensions calculées.

Les exclusions sont appliquées symétriquement à travers les quatre quadrants.

Exclusions symétriques :

Les exclusions sont réparties uniformément dans un quadrant puis reproduites dans les autres quadrants pour préserver la symétrie.

Tracé des points :

Les points valides sont tracés en bleu et les points exclus en rouge.

Les axes et la grille sont ajoutés pour une meilleure lisibilité.

Résultats Visuels

Diagramme QAM pour 



Points bleus : Symboles valides utilisés pour la modulation.

Points rouges : Symboles exclus selon les règles définies.

Exemple de Sortie du Terminal



Le terminal affiche les dimensions de la grille et les exclusions pour chaque puissance :

Puissance | Lignes | Colonnes | Soustraction
-------------------------------------------
    2     |   2    |    2     |      0     
    3     |   4    |    4     |      8     
    4     |   4    |    4     |      0     
    5     |   6    |    6     |      4     
    6     |   8    |    8     |      0     
    7     |  12    |   12     |     16     
    9     |  24    |   24     |     64     

Utilisation

Prérequis

Python 3.x

Bibliothèques nécessaires : matplotlib, numpy

Instructions

Clonez ce dépôt ou téléchargez les fichiers source.

Installez les dépendances nécessaires via pip :

pip install matplotlib numpy

Exécutez le script principal :

python script_qam.py

Cela affichera les résultats calculés pour chaque puissance et générera les diagrammes correspondants.

Comment Lire un Diagramme QAM

Axes :

L'axe horizontal représente la composante en phase (In-Phase, I).

L'axe vertical représente la composante quadrature (Quadrature, Q).

Points bleus : Les symboles disponibles pour la transmission.

Points rouges : Les symboles exclus pour maintenir la symétrie ou optimiser la modulation.

Grille : La structure sous-jacente de la constellation.

Auteur

Ce script a été conçu pour explorer les constellations QAM et leurs ajustements spécifiques. Si vous avez des questions ou des suggestions, n'hésitez pas à ouvrir une issue ou à soumettre une pull request.

