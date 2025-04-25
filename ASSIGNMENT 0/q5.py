#5. PYTHON PROGRAM TO PRINT TABLE OF ANY NO.

#function to print table
def table(n:int):

    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")

#taking user's input
num = int(input("Enter a number:"))

#function calling
table(num)