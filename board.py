from cell import Cell
import random


#   Classe représentant le plateau de jeu du démineur.
class Board:

    #   Initialise le plateau de jeu.
    #   :param size: Taille du plateau de jeu.
    #   :param num_mines: Nombre de mines sur le plateau. 
    def __init__(self, size, num_mines):
        self.size = size
        self.num_mines = num_mines
        self.grid = [[Cell() for _ in range(size)] for _ in range(size)]
        self.place_mines()

    #   Place aléatoirement les mines sur le plateau et met à jour le nombre de mines adjacentes pour chaque cellule.
    def place_mines(self):
        positions = random.sample(range(self.size * self.size), self.num_mines)
        for pos in positions:
            row = pos // self.size
            col = pos % self.size
            self.grid[row][col].is_mine = True
            self.update_adjacent_mines(row, col)

    
    #   Met à jour le nombre de mines adjacentes pour une cellule spécifique sur le plateau.
    #   :param row: L'index de la ligne de la cellule.
    #   :param col: L'index de la colonne de la cellule.
    def update_adjacent_mines(self, row, col):
        deltas = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if i != 0 or j != 0]
        for dr, dc in deltas:
            r, c = row + dr, col + dc
            if 0 <= r < self.size and 0 <= c < self.size and not self.grid[r][c].is_mine:
                self.grid[r][c].adjacent_mines += 1

    
    #   Révèle une cellule spécifique sur le plateau.
    #   :param row: L'index de la ligne de la cellule.
    #   :param col: L'index de la colonne de la cellule.
    def reveal_cell(self, row, col):
        if 0 <= row < self.size and 0 <= col < self.size:
            cell = self.grid[row][col]
            if not cell.is_revealed:
                cell.reveal()
                if cell.adjacent_mines == 0:
                    self.reveal_adjacent_cells(row, col)

    
    #   Révèle toutes les cellules adjacentes à une cellule spécifique sur le plateau.
    #   :param row: L'index de la ligne de la cellule.
    #   :param col: L'index de la colonne de la cellule.
    def reveal_adjacent_cells(self, row, col):
        deltas = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if i != 0 or j != 0]
        for dr, dc in deltas:
            r, c = row + dr, col + dc
            self.reveal_cell(r, c)

    #   Représentation visuelle du plateau de jeu.
    def __repr__(self):
        return '\n'.join(' '.join(str(cell) for cell in row) for row in self.grid)

    #   Vérifie si toutes les cellules non-minées ont été révélées, ce qui signifie que le joueur a gagné.
    #   :return: True si le joueur a gagné, False sinon.
    def check_win(self):
        for row in range(self.size):
            for col in range(self.size):
                if not self.grid[row][col].is_mine and not self.grid[row][col].is_revealed:
                    return False
        return True
