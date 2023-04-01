import random

def compare(guess,answer) :
    if guess > answer :
        return "Too high"
    elif guess < answer :
        return "Too low" 
    elif guess == answer :
        return "You won"
    else :
        return "Invalid input"

   

def game() :
    print("Welcome to the number guessing game")
    print("I am thinking of a number between 1 and 100")

    difficulty = input("Choose a difficutly.Type 'easy' or 'hard' : ")

    if difficulty == "easy" :
        no_of_attempts = 9
    elif difficulty == "hard" :
        no_of_attempts = 4
    else :
        print("Please enter the correct word")

    answer = random.randint(1,100)
    while no_of_attempts != -1 :
        guess = int(input("Make a guess : "))
        print(compare(guess,answer))
        if compare(guess,answer) == "You won" :
            return 
        if no_of_attempts == 0 :
            print(f"You lose.the answer is {answer}")
            return
        print(f"You still have {no_of_attempts} attempts.")
        no_of_attempts -= 1

game()

    







