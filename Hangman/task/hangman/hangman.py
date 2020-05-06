# Hangman.py
# Written by Natasha Graham
# Project from JetBrains Hyperskills course
import random


def list_to_string(letters):
    result = ""
    for letter in letters:
        result = result + letter
    return result


def play_game():
    wordlist = ["python", "java", "kotlin", "javascript"]
    word = random.choice(wordlist)
    word_revealed = list("-"*len(word))
    word_letters = set(word)
    tries = 8
    guessed = set()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    while tries > 0:
        print()
        print(list_to_string(word_revealed))
        guess = input("Input a letter: ")
        if len(guess) != 1:
            print("You should print a single letter")
            continue
        elif guess in word_letters:
            word_letters.remove(guess)
            guessed.add(guess)
            i = 0
            for char in word:
                if char not in word_letters:
                    word_revealed[i] = char
                i += 1
        elif guess in guessed:
            print("You already typed this letter")
            continue
        elif guess not in alphabet:
            print("It is not an ASCII lowercase letter")
            continue
        else:
            print("No such letter in the word")
            guessed.add(guess)
            tries -= 1
        if len(word_letters) == 0:
            break

    if tries == 0:
        print("You are hanged!")
    else:
        print()
        print(word)
        print("You guessed the word!")
        print("You survived!")


print("H A N G M A N")
exit_game = False
while not exit_game:
    choice = input('Type "play" to play the game, "exit" to quite: ')
    if choice == "exit":
        exit_game = True
    elif choice == "play":
        play_game()
