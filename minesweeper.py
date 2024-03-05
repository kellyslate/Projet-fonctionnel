import tkinter as tk
from tkinter import messagebox
from board import Board


#   Class representant l'interface graphique du jeu.
class MineSweeperGUI:

    # Initialise l'interface utilisateur du Démineur.
    # :param master: Fenêtre principale de l'application.
    # :param size: Taille du plateau de jeu (par défaut 20x20).
    # :param num_mines: Nombre de mines sur le plateau (par défaut 50).
    def __init__(self, master, size=20, num_mines=50):
        self.master = master
        self.board = Board(size, num_mines)
        self.size = size
        self.num_mines = num_mines
        self.buttons = [[None for _ in range(size)] for _ in range(size)]
        self.create_widgets()

    # Crée les boutons représentant les cases du jeu.
    def create_widgets(self):
        for row in range(self.size):
            for col in range(self.size):
                button = tk.Button(self.master, width=2, command=lambda r=row, c=col: self.on_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    # Met à jour l'affichage des boutons après chaque coup.
    def update_buttons(self):
        for row in range(self.size):
            for col in range(self.size):
                cell = self.board.grid[row][col]
                if cell.is_revealed:
                    self.buttons[row][col].config(text=str(cell), state="disabled")
                else:
                    self.buttons[row][col].config(text="", state="normal")

    # Gère l'action lorsqu'un bouton est cliqué.
    # :param row: Ligne du bouton cliqué.
    # :param col: Colonne du bouton cliqué.
    def on_click(self, row, col):
        cell = self.board.grid[row][col]
        if cell.is_mine:
            self.reveal_all()
            self.show_message("You Loose !")
        else:
            self.board.reveal_cell(row, col)
            self.update_buttons()
            if self.board.check_win():
                self.show_message("Congratulations! You Win !")

    # Révèle toutes les cases du jeu après la fin de la partie en cas de défaite.
    def reveal_all(self):
        for row in range(self.size):
            for col in range(self.size):
                self.board.grid[row][col].is_revealed = True
        self.update_buttons()

    # Affiche une boîte de dialogue avec un message.
    # :param message: Message à afficher dans la boîte de dialogue.
    def show_message(self, message):
        messagebox.showinfo("Game Over", message)
        self.master.quit()


