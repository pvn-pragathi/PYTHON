#Faulty Code

# for number in range(1,101):
#     if number % 5 == 0 or number % 3 == 0:
#         print("FIZZBUZZ")
#     if number % 5 == 0:
#         print("BUZZ")
#     if number % 3 == 0:
#         print("FIZZ")
#     else:
#         print([number])

#Correct Code

for number in range(1,101) :
    if number % 5 == 0 and number % 3 == 0 :
        print("FIZZBUZZ")
    elif number % 5 == 0 :
        print("BUZZ")
    elif number % 3 == 0 :
        print("FIZZ")
    else :
        print(number)

    