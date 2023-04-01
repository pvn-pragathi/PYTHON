import random
from replit import clear

def deal_card() :
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards) :
    if sum(cards) == 21 and len(cards) == 2 :
        return 0

    if 11 in cards and sum(cards) > 21 :
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(player_score,computer_score) :
    if player_score == computer_score :
        return "It's a draw"
    elif computer_score == 0 :
        return "Lose,opponent has a blackjack"
    elif player_score == 0 :
        return "Win with a blackjack"
    elif player_score > 21 :
        return "You went over!You lose"
    elif computer_score > 21 :
        return "Win,the computer got busted"
    elif player_score > computer_score :
        return "You win"
    else :
        return "You lose"

def play_game() :

    player_cards = []
    computer_cards = []

    for _ in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())

    is_game_over = False
    while not is_game_over :

        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards : {player_cards},current score : {player_score}")
        print(f"The computer's first card is {computer_cards[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21 :
            is_game_over = True
        else :
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass : ")
            if user_should_deal == "y" :
                player_cards.append(deal_card())
            else :
                is_game_over = True

    while computer_score != 0 and computer_score < 17 :
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)


    print(f"Your final hand : {player_cards},final_score : {player_score}")
    print(f"Computer final hand : {computer_cards},computer score : {computer_score}")
    print(compare(player_score,computer_score))


while input("Do you want to play the game of blackjack?Type 'y' for yes and 'n' for no.") == "y" :
    clear()
    play_game()








    


    


