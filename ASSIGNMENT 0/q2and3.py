#2. PYTHON PROGRAM TO FIND THE FACTORIAL OF A NUMBER

#a recursive function to find factorial
def factorial(n):
    while n>0:
        fac=n*factorial(n-1)
    return fac

#taking user input
num = int(input("Enter a number to find it's factorial: "))

#function calling
result = factorial(num)
print(f"The factorial is {result}")