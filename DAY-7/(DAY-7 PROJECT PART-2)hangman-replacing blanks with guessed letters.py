import random


#Basic stuff
word_list = ["ardark","baboon","camel"]


#To choose a random wprd.
chosen_word = random.choice(word_list)


#To print the number of blanks
display = []
for add in chosen_word:
    display += "_"

print(display)


#Input of users' guess.
user_letter = input("Guess a letter : ").lower()


#To replace the blanks with correct words
x = 0 
for replace in chosen_word:
    if replace == user_letter:
        display[x] = replace
    x += 1

print(display)