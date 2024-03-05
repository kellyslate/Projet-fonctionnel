#   Classe représentant les différentes cellules du plateau.
class Cell:

    #   Initialise une cellule du plateau de jeu du Démineur.
    #   :param is_mine: Indique si la cellule contient une mine (par défaut False).
    #   :param is_revealed: Indique si la cellule a été révélée (par défaut False).
    def __init__(self, is_mine=False, is_revealed=False):
        self.is_mine = is_mine
        self.is_revealed = is_revealed
        self.adjacent_mines = 0 

    # Représentation textuelle de la cellule.
    # Si la cellule est révélée, affiche le nombre de mines adjacentes ou une mine.
    # Si la cellule n'est pas révélée, affiche 'X'.
    def __repr__(self):
        if self.is_revealed:
            if self.is_mine:
                return "💣" 
            else:
                return str(self.adjacent_mines) if self.adjacent_mines > 0 else "-" 
        else:
            return "X"  

    # Révèle la cellule en mettant à jour son état 'is_revealed' à True.
    def reveal(self):
        self.is_revealed = True
