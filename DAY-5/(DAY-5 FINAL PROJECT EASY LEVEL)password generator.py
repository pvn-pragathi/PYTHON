#basic stuff required to complete the project.
import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#Actual logic and solving

#To generate the random letters
selected_letters = ""
for letter in range(0,nr_letters):
    selected_letters += random.choice(letters)


#To generate the random numbers
selected_numbers = ""
for number in range(0,nr_numbers):
    selected_numbers += random.choice(numbers)


#To generate the random symbols
selected_symbols = ""
for symbol in range(0,nr_numbers):
    selected_symbols += random.choice(symbols)


#To generate the whole password
print(f"Your password is : {selected_letters}{selected_numbers}{selected_symbols}")

