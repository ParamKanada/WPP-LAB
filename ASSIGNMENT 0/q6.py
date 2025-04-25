#6. PYTHON PROGRAM TO REVERSE OF A GIVEN NO

#taking user's input
num = int(input("Enter the number:"))

temp = num
rev_num=0
while temp%10 != 0:
    rev_num = rev_num*10 + temp%10
    temp//=10

#printing the reversed number
print(f"The reversed number is: {rev_num}")