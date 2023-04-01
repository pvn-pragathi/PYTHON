import random
#Basic stuff
word_list = [
"mango",
"apple",
"banana",
"pear",
"grapes",
"orange",
"drink",
"father",
"mother",
"honey",
"mobile",
"keyboard",
"phone",
"tiger",
"lion",
"map",
"body",
]

#To choose a random wprd.
chosen_word = random.choice(word_list)

#ASCII arts
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


#To print the number of blanks
display = []
for add in chosen_word:
    display += "_"

print(display)

lives = 6
end_of_game = False

while not end_of_game :
    print(stages[lives])
    user_letter = input("Guess a letter : ").lower()
    x = 0 
    for replace in chosen_word:
        if replace == user_letter:
            display[x] = replace  
        x += 1
    print(display)

    if user_letter not in chosen_word:
        lives -= 1
        

    if "_" in display :
        end_of_game = False
    else:
        end_of_game = True
        print("You won")

    if lives == 0:
            end_of_game = True
            print(stages[0])
            print("You lose!")
            print(f"The word is {chosen_word}")

    


    
    


        
    








