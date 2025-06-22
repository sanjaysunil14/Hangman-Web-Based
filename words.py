easy_words = ['cat', 'dog', 'sun', 'cup']
medium_words = ['water', 'board', 'player', 'python']
hard_words = ['computer', 'mathematics', 'programming', 'condition']

def get_words_by_difficulty(level):
    if level == "easy":
        return easy_words
    elif level == "medium":
        return medium_words
    elif level == "hard":
        return hard_words
    else:
        return medium_words
