import tkinter as tk
from tkinter import messagebox
from game_logic import WordGame
from words import get_words_by_difficulty
import random

class WordGuessApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Guessing Game")
        self.root.geometry("400x400")
        self.create_difficulty_screen()

    def create_difficulty_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Select Difficulty Level", font=("Helvetica", 16)).pack(pady=20)
        for level in ['easy', 'medium', 'hard']:
            tk.Button(self.root, text=level.capitalize(),
                      command=lambda l=level: self.start_game(l),
                      width=15, font=("Helvetica", 12)).pack(pady=5)

    def start_game(self, level):
        word = random.choice(get_words_by_difficulty(level))
        self.game = WordGame(word)
        self.build_game_screen()

    def build_game_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.status_label = tk.Label(self.root, text="Turns left: 12", font=("Helvetica", 14))
        self.status_label.pack(pady=10)

        self.word_display = tk.Label(self.root, text=self.game.display_word(), font=("Courier", 24))
        self.word_display.pack(pady=20)

        self.entry = tk.Entry(self.root, font=("Helvetica", 16), width=5, justify='center')
        self.entry.pack()

        self.guess_button = tk.Button(self.root, text="Guess", command=self.make_guess)
        self.guess_button.pack(pady=10)

        self.restart_button = tk.Button(self.root, text="Restart", command=self.create_difficulty_screen)
        self.restart_button.pack(pady=10)

    def make_guess(self):
        ch = self.entry.get().strip()
        self.entry.delete(0, tk.END)

        correct, msg = self.game.guess_char(ch)
        self.word_display.config(text=self.game.display_word())
        self.status_label.config(text=f"Turns left: {self.game.turns}")

        if self.game.status == 'won':
            messagebox.showinfo("Result", f"🎉 You won! The word was '{self.game.word}'")
            self.create_difficulty_screen()
        elif self.game.status == 'lost':
            messagebox.showerror("Result", f"❌ You lost! The word was '{self.game.word}'")
            self.create_difficulty_screen()

if __name__ == "__main__":
    root = tk.Tk()
    app = WordGuessApp(root)
    root.mainloop()
