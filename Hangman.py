import random


def draw_head(state):
    if (state == 0):
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
    if (state == 0):
        print("    |     ")
        print("    |     ")
        print("    |     ")
        print("    |     ")
        print("    |     ")
        print("    |     ")
    elif (state == 1):
        print("    |       |  ")
        print("    |       |")
        print("    |       |")
        print("    |       |")
        print("    |       |")
        print("    |       |")
    elif (state == 2):
        print("    |       | ")
        print("    |      /| ")
        print("    |     / | ")
        print("    |    /  | ")
        print("    |       |")
        print("    |       |")
    elif (state == 3):
        print("    |       |  ")
        print("    |      /|\\")
        print("    |     / | \\")
        print("    |    /  |  \\")
        print("    |       |")
        print("    |       |")


def draw_legs(state):
    if (state == 0):
        print("    |   ")
        print("    |   ")
        print("    |   ")
        print("    |   ")
        print("    |")
        print("    |")
        print("____|____")
    elif (state == 1):
        print("    |      / ")
        print("    |     /  ")
        print("    |    /   ")
        print("    |   /    ")
        print("    |")
        print("    |")
        print("____|____")
    elif (state == 2):
        print("    |      / \\")
        print("    |     /   \\")
        print("    |    /     \\")
        print("    |   /       \\")
        print("    |")
        print("    |")
        print("____|____")

def hide_words(mystery):
    for letter in range( 0, len(mystery)):
        if mystery[letter].isalpha():
            mystery = mystery[:letter] + "_" + mystery[letter + 1:]
        letter += 1

    return mystery

def main():
    file = open("Dictionary.txt", "r+")
    lines = file.readlines()
    #word = random.choice(lines)[:-1]
    word = lines[960][:-1]
    mystery = word
    print(word)
    print("Word is %s and is %d letters long" %(word, len(word)))

    mystery = hide_words(mystery)

    print(mystery)

if __name__ == "__main__":
    main()
