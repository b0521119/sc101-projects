"""
File: hangman.py
Name: Jennifer Chueh
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""

import random

# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program is to create a hangman game.
    """
    count_initial()
    guess_word()  # Play the game


def dashed_random_word(string):  # Let the word become dashed
    dashed = ''
    for i in range(len(string)):
        dashed = dashed + '-'
    return dashed


def guess_word():
    guess_string = random_word()  # original word
    dashed_string = dashed_random_word(guess_string)

    count = N_TURNS
    print("The word looks like: " + dashed_string)
    print("You have " + str(N_TURNS) + " guesses left.")

    while True:
        input_ch = input("Your guess: ")
        s = input_ch.upper()
        if not s.isalpha() or len(s) > 1:
            print("Illegal Format.")
        else:
            if guess_string.find(s) == -1:
                print("There is no " + s + "'s in the word.")
                count -= 1
                if count == 7:
                    count_initial()
                if count == 6:
                    count_6_graphic()
                if count == 5:
                    count_5_graphic()
                if count == 4:
                    count_4_graphic()
                if count == 3:
                    count_3_graphic()
                if count == 2:
                    count_2_graphic()
                if count == 1:
                    count_1_graphic()
                if count == 0:
                    lose_graphic()
                    print("You are completely hung :( ")
                    print("Try it next time!")
                    print("The word was: " + guess_string)
                    break
            elif guess_string.find(s) != -1:
                if count == 7:
                    count_initial()
                if count == 6:
                    count_6_graphic()
                if count == 5:
                    count_5_graphic()
                if count == 4:
                    count_4_graphic()
                if count == 3:
                    count_3_graphic()
                if count == 2:
                    count_2_graphic()
                if count == 1:
                    count_1_graphic()
                print("You are correct! Great Job!")
                ans = ''
                for i in range(len(guess_string)):
                    if s == guess_string[i]:
                        ans = ans + s
                    else:
                        ans = ans + dashed_string[i]
                dashed_string = ans
                if dashed_string == guess_string:
                    win_graphic()
                    print("You win!")
                    print("The word was: " + guess_string)
                    break
                print("The word looks like: " + dashed_string)
            print("You have " + str(count) + " guesses left.")


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


def count_initial():
    print("========")
    for i in range(6):
        print("|")


def count_6_graphic():
    print("========")
    print("|    |")
    for i in range(5):
        print("|")


def count_5_graphic():
    print("========")
    print("|    |")
    print("|   ( )")
    for i in range(4):
        print("|")


def count_4_graphic():
    print("========")
    print("|    |")
    print("|   ( )")
    print("|    #")
    print("|    #")
    print("|")
    print("|")


def count_3_graphic():
    print("========")
    print("|    |")
    print("|   ( )")
    print("|   ~#~")
    print("|    #")
    print("|")
    print("|")


def count_2_graphic():
    print("========")
    print("|    |")
    print("|   ( )")
    print("|   ~#~")
    print("|    #")
    print("|   / \\")
    print("|")


def count_1_graphic():
    print("========")
    print("|    |")
    print("|  (0.0)")
    print("|   ~#~")
    print("|    #")
    print("|   / \\")
    print("|")


def lose_graphic():
    print("========")
    print("|    |")
    print("|  (X.X)")
    print("|   |||")
    print("|    |")
    print("|   / \\")
    print("|")


def win_graphic():
    print(" \Thank you!/")
    print("    ($.$)")
    print("     \|/")
    print("      |")
    print(" ... / \\")


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
