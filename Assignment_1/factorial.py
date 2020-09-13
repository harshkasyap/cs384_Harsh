# Python program to find the factorial of a number provided by the user.

def factorial(num):
    #Logic for the factorial program
    
    factorial = 1

    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,num + 1):
            factorial = factorial*i
    print("The factorial of",num,"is",factorial)

# To take input from the user
num = int(input("Enter a number: "))

factorial(num)
