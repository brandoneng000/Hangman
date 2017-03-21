import random


def drawHead(state):
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


def drawBodyAndArms(state):
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


def drawLegs(state):
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


def main():
    file = open("Dictionary.txt", "r+")
    lines = file.readlines()
    #word = random.choice(lines)[:-1]
    word = lines[960][:-1]
    mystery = word
    print(word)
    print("Word is %s and is %d letters long" %(word, len(word)))

    for letter in range( 0, len(mystery)):
        if mystery[letter].isalpha():
            mystery = mystery[:letter] + "_" + mystery[letter + 1:]
        letter += 1

    print(mystery)

if __name__ == "__main__":
    main()
