import random


#Basic stuff
word_list = ["ardark","baboon","camel"]


#To choose a random wprd.
chosen_word = random.choice(word_list)


#Input of users' guess.
user_letter = input("Guess a etter : ").lower()

#Checking each letter in computer word with user's letter and printing the result.
for letter in chosen_word :
    if user_letter == chosen_word :
        print("Right")
    else :
        print("Wrong")
