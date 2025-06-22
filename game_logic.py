import random

class WordGame:
    def __init__(self, word):
        self.word = word.lower()
        self.guesses = set()
        self.turns = 12
        self.status = 'playing'

    def guess_char(self, ch):
        ch = ch.lower()
        if ch in self.guesses or len(ch) != 1 or not ch.isalpha():
            return False, "Invalid or repeated guess."

        self.guesses.add(ch)

        if ch not in self.word:
            self.turns -= 1
            if self.turns == 0:
                self.status = 'lost'
            return False, "Incorrect"

        if all(c in self.guesses for c in self.word):
            self.status = 'won'
        return True, "Correct"

    def display_word(self):
        return ' '.join([c if c in self.guesses else '_' for c in self.word])
