# Démineur Fonctionnel

Ce projet est une implémentation du jeu Démineur en Python utilisant une approche fonctionnelle avec des méthodes pures.

## Méthodes Pures :

Les méthodes comme reveal_cell() et update_buttons() dans MineSweeperGUI, ainsi que update_adjacent_mines() dans Board, ne modifient pas l'état interne de l'objet (à l'exception de la modification de is_revealed), mais retournent plutôt de nouvelles valeurs ou effectuent des actions en fonction de leurs paramètres. Cela les rend similaires à des fonctions pures, car elles ne dépendent que des données qu'elles reçoivent et ne modifient pas l'état global de l'application.
Séparation des Préoccupations :

## Utilisation d'Objets Immutables :

Bien que les objets ne soient pas strictement immuables (puisque certains attributs sont modifiés), leur état global n'est pas directement altéré par les méthodes. Par exemple, lorsqu'une cellule est révélée dans le jeu, l'objet cellule lui-même n'est pas modifié ; plutôt, l'attribut is_revealed de la cellule est modifié. Cela peut être considéré comme une approche fonctionnelle dans la mesure où les objets restent cohérents et isolés dans leur état.


## Fonctionnalités

- Plateau de jeu de taille configurable.
- Nombre de mines ajustable.
- Interface graphique simple avec Tkinter.
- Utilisation de méthodes pures pour gérer la logique du jeu.

## Comment jouer

1. Exécutez le script `main.py` pour lancer le jeu.
2. Cliquez sur les cases pour les révéler.
3. Évitez les mines et révélez toutes les cases pour gagner.

## Structure du code

- `main.py` : Point d'entrée de l'application. Crée une instance de l'interface graphique du Démineur.
- `board.py` : Contient la classe `Board`, qui représente le plateau de jeu.
- `cell.py` : Contient la classe `Cell`, qui représente une cellule du plateau de jeu.
- `minesweeper_gui.py` : Contient la classe `MineSweeperGUI`, qui gère l'interface graphique du jeu.

## Installation

1. Assurez-vous d'avoir Python installé sur votre système.
2. Clonez ce dépôt :
3. Accédez au répertoire du projet :
4. Exécutez le jeu :

