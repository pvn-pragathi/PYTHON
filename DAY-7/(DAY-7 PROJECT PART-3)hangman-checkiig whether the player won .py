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


#Initially it is false and using this variable we can make the while loop run until it is true.We can update that in the while loop that "until there are _ in display list it is false in case no _ it is set to true."That means while loop needs breaker for that loop within that loop.
end_of_game = False

while not end_of_game :
    user_letter = input("Guess a letter : ").lower()
    x = 0 
    for replace in chosen_word:
        if replace == user_letter:
            display[x] = replace
        x += 1
    print(display)

    if "_" in display :
        end_of_game = False
    else:
        end_of_game = True
    



