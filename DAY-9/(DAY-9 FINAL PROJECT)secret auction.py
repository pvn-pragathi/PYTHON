# from repit import clear

print("Welcome to secret auction program! \n")

entries = {}



def check_winner() :

    highest_bid = 0
    for entry in entries :
        bid_amount = entries[entry]
        if bid_amount > highest_bid :
            highest_bid = bid_amount
            winner = entry
    print(f"The winner is {winner} with a bid amount of {highest_bid}")

should_add_person = True
while should_add_person :

    person_name = input("Enter your name : \n")
    person_bid_amount = int(input("Enter your bid amount : \n$"))
    should_add = input("Enter 'Yes' if you want to add another person otherwise enter 'No' : \n").lower()
    # clear()

    entries[person_name] = person_bid_amount

    if should_add == "no" :
        should_add_person = False
        check_winner()

        

        

            

    




