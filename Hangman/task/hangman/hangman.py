# Write your code here
import random


def list_to_string(letters):
    result = ""
    for letter in letters:
        result = result + letter
    return result


wordlist = ["python", "java", "kotlin", "javascript"]
word = random.choice(wordlist)
word_revealed = list("-"*len(word))
word_letters = set(word)
tries = 8
guessed = set()

print("H A N G M A N")

while tries > 0:
    print()
    print(list_to_string(word_revealed))
    guess = input("Input a letter: ")
    if guess in word_letters:
        word_letters.remove(guess)
        guessed.add(guess)
        i = 0
        for char in word:
            if char not in word_letters:
                word_revealed[i] = char
            i += 1
    elif guess in guessed:
        print("No improvements")
        tries -= 1
    else:
        print("No such letter in the word")
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
