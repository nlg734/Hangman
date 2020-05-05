# Write your code here
import random


wordlist = ["python", "java", "kotlin", "javascript"]
word = random.choice(wordlist)


print("H A N G M A N")
guess = input("Guess the word {}: ".format(word[0:3]+"-"*(len(word)-3)))

if word == guess:
    print("You survived!")
else:
    print("You are hanged!")
