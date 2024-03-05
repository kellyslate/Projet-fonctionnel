import tkinter as tk
from tkinter import messagebox
from board import Board
from minesweeper import MineSweeperGUI


def main():
    root = tk.Tk()
    root.title("Minesweeper")
    game = MineSweeperGUI(root)
    game.update_buttons()
    root.mainloop()

if __name__ == "__main__":
    main()