import random
import sys

attempts = 0
file = open("Dictionary.txt", "r+")
word = ""
mystery = ""


def draw_head(state):
    if state == 0:
        print("    _________")
        print("    |       |")
        print("    |       |")
        print("    |       |")
        print("    |      ")
        print("    |      ")
        print("    |      ")
        print("    |      ")
    else:
        print("    _________")
        print("    |       |")
        print("    |       |")
        print("    |      _|_")
        print("    |     /   \\")
        print("    |    |     |")
        print("    |     \___/")
        print("    |       |  ")


def draw_body_and_arms(state):
    if state == 0:
        print("    |     ")
        print("    |     ")
        print("    |     ")
        print("    |     ")
        print("    |     ")
        print("    |     ")
    elif state == 1:
        print("    |       |  ")
        print("    |       |")
        print("    |       |")
        print("    |       |")
        print("    |       |")
        print("    |       |")
    elif state == 2:
        print("    |       | ")
        print("    |      /| ")
        print("    |     / | ")
        print("    |    /  | ")
        print("    |       |")
        print("    |       |")
    elif state == 3:
        print("    |       |  ")
        print("    |      /|\\")
        print("    |     / | \\")
        print("    |    /  |  \\")
        print("    |       |")
        print("    |       |")


def draw_legs(state):
    if state == 0:
        print("    |   ")
        print("    |   ")
        print("    |   ")
        print("    |   ")
        print("    |")
        print("    |")
        print("____|____")
    elif state == 1:
        print("    |      / ")
        print("    |     /  ")
        print("    |    /   ")
        print("    |   /    ")
        print("    |")
        print("    |")
        print("____|____")
    elif state == 2:
        print("    |      / \\")
        print("    |     /   \\")
        print("    |    /     \\")
        print("    |   /       \\")
        print("    |")
        print("    |")
        print("____|____")


def hide_words(myst):
    for letter in range(0, len(myst)):
        if myst[letter].isalpha():
            myst = myst[:letter] + "_" + myst[letter + 1:]
        letter += 1

    return myst


def draw_hangman():
    global attempts
    game_state = 1
    if attempts == 0:
        draw_head(0)
        draw_body_and_arms(0)
        draw_legs(0)
    elif attempts >= 1:
        draw_head(1)
        if attempts == 1:
            draw_body_and_arms(0)
        elif attempts == 2:
            draw_body_and_arms(1)
        elif attempts == 3:
            draw_body_and_arms(2)
        elif attempts >= 4:
            draw_body_and_arms(3)

        if attempts == 5:
            draw_legs(1)
        elif attempts == 6:
            draw_legs(2)
            game_state = 0
        else:
            draw_legs(0)

    return game_state


def letter_check(myst, origin, char):
    global attempts
    counter = 0
    for letter in range(0, len(myst)):
        if origin[letter] == char or origin[letter] == char.upper():
            myst = myst[:letter] + char + myst[letter + 1:]
            counter += 1

    if counter == 0:
        attempts += 1

    return myst


def get_guess():
    guess = input("What letter do you guess? ")
    while not guess.isalpha() or len(guess) != 1:
        print("Please enter a single letter")
        guess = input("What letter do you guess? ")

    return guess.lower()


def initialize_game():
    global mystery
    global word

    lines = file.readlines()
    word = random.choice(lines)[:-1].lower()
    word = lines[0][:-1].lower()
    mystery = hide_words(word)
    print("Guess what the word is?")
    print(mystery)


def main():
    global mystery
    global word
    lose = draw_hangman()

    initialize_game()
    while mystery != word and lose == 1:
        guess = get_guess()
        mystery = letter_check(mystery, word, guess)
        print("Current status is %s" % mystery)
        lose = draw_hangman()

    if mystery == word:
        print("Congratulations!!! You Win!!!")
    elif lose == 0:
        print("You Lose!!! The word was", word)


if __name__ == "__main__":
    main()
