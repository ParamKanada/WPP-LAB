t = int(input("Enter the number of test cases: "))

numbers=[]

for i in range(t):
    num_st = input("Enter number:")
    n= int(num_st)
    for j in num_st:
        if n%int(j)==0:
            numbers.append(n)
            break

print(numbers)