
from game_data import data
import random
from replit import clear

def new_personality() :
    return random.choice(data)

def check_answer(dict1,dict2,guess) :
    follower_count1 = dict1["follower_count"]
    follower_count2 = dict2["follower_count"]

    if follower_count1 > follower_count2 :
        return guess == "a"
    elif follower_count1 < follower_count2 :
        return guess == "b"

def format_data(personality) :
    name = personality["name"]
    decription = personality["description"]
    country = personality["country"]

    return f"{name}, a {decription} from {country}"



    
next_person = new_personality()

is_game_over = False
score = 0
while not is_game_over :

    first_person = next_person
    next_person = new_personality()

    while first_person == next_person :
        next_person = new_personality()

    while first_person["follower_count"] == next_person["follower_count"] :
        first_person = new_personality()
    
    print(f"Compare A : {format_data(first_person)}")
    print("VS")
    print(f"Compare B : {format_data(next_person)}")

    guess = input("Type 'A' or 'B' : ").lower()

    answer = check_answer(first_person,next_person,guess)

    if answer == True :
        score += 1
        print(f"You are right.Current score : {score}")
    else :
        print(f"Sorry!That's wrong.Your score is {score}")
        is_game_over = True

        

    













