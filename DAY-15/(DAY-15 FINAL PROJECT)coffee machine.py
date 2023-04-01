MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def ask_money():
    print("Please insert coins.")

    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01

    return total


def report(resource):
    global profit
    print(f"Water : {resource['water']}")
    print(f"Milk : {resource['milk']}")
    print(f"Coffee : {resource['coffee']}")
    print(f"Money : {profit}")


def are_ingredients_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry,there is not enough {item}")
            return False
    return True


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


def is_transaction_successful(money_received, drink_cost):
    global profit
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} change")
        profit += money_received
        return True
    else:
        print("Sorry that's not enough money.Money refunded")
        return False


on = True
while on:
    user_choice = input("What would you like? (espresso/latte/cappuccino) :")

    if user_choice == "report":
        report(resources)
    elif user_choice == "Off":
        on = False
    else:
        drink = MENU[user_choice]
        if are_ingredients_sufficient(drink["ingredients"]):
            payment = ask_money()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(user_choice, drink["ingredients"])










