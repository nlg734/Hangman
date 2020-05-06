# Write your code here
import random

def word_to_print(a_list):
    result = ""
    for char in a_list:
        result = result + char
    return result

wordlist = ["python", "java", "kotlin", "javascript"]
word = random.choice(wordlist)
word_revealed = list("-"*len(word))
word_letters = set(word)

print("H A N G M A N")
print()
#guess = input("Guess the word {}: ".format(word[0:3]+"-"*(len(word)-3)))

for tries in range(8):
    print(word_to_print(word_revealed))
    guess = input("Input a letter: ")
    if guess in word_letters:
        word_letters.remove(guess)
        i = 0
        for char in word:
            if char not in word_letters:
                word_revealed[i] = char
            i += 1
    else:
        print("No such letter in the word")
    print()

print("Thanks for playing!")
print("We'll see how well you did in the next stage")

# if word == guess:
#     print("You survived!")
# else:
#     print("You are hanged!")

