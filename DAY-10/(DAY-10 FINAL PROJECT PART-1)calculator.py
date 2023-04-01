
def add(n1,n2) :
    return n1 + n2

def subtract(n1,n2) :
    return n1 - n2

def multiply(n1,n2) :
    return n1 * n2

def divide(n1,n2) :
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "x" : multiply,
    "/" : divide,
}

def calculator() :

    num1 = float(input("What's the first number : "))

    for operation in operations :
        print(operation)

    symbol = input("Pick an operation from the line above : ")

    num2 = float(input("What's the second number : "))

    calculation_function = operations[symbol]
    first_num = calculation_function(num1,num2)

    print(f"{num1} {symbol} {num2} = {first_num}")

    should_continue = True
    while should_continue :

        continue_input = input(f"Type 'y' to continue calculating with {first_num} otherwise type 'n' to start a new calculator :  ")
        if continue_input == "n" :
            calculator()

        symbol = input("Pick another operation : ")
        next_num = int(input("What's the next number : "))

        calculation_function = operations[symbol]
        answer2 = calculation_function(first_num,next_num)

        print(f"{first_num} {symbol} {next_num} = {answer2}")

        first_num = answer2


calculator()



    
        