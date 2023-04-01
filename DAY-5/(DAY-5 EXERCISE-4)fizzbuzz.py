#The whole game and logic
#Taking the numbers first from 1 to 1oo
for numbers in range(1,101):
#checking whether the number is divisible by 5 and 3,if no go to next condition, if yes print FIZZBUZZ instead of the actual number.
    if numbers % 5 == 0 and numbers % 3 == 0:
        print("FIZZBUZZ")
#checking whether the number is divisible by 5,if no go to next condition, if yes print BUZZ instead of the actual number.
    elif numbers % 5 == 0:
        print("BUZZ")
#checking whether the number is divisible by 3,if no go to next condition, if yes print FIZZ instead of the actual number.
    elif numbers % 3 == 0:
        print("FIZZ")
#if none of the conditions are true just print the actual number.
    else:
        print(numbers)
















































    # if numbers % 3 :
    #     print("FIZZ")
    #     if numbers % 5 :
    #         print("BUZZ")
    #         if numbers % 5 and 3 :
    #             print("FIZZBUZZ")
    # else :
    #     print(numbers)


