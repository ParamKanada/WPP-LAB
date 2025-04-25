def max_xor(x,y):
    max_val=0
    for a in range (x,y+1):
        for b in range(a,y+1):
            max_val=max(max_val,a^b)
    return max_val

def decimalToBinary(n):
    bin_str = ""  # Make an empty string
    temp = n
    while temp > 0:
        remainder = int(temp % 2)  # Ensure remainder is an integer
        bin_str = str(remainder) + bin_str  # Prepend(because reminder is added in front) to the string
        temp = temp // 2  # Integer division

    if bin_str == "": #handle if number is 0
      bin_str = "0"

    return(bin_str) #no need to reverse string

L,R=int(input("Enter L: ")),int(input("Enter R: "))

print(f"{L} = {decimalToBinary(L)}\t{R} = {decimalToBinary(R)}")
result=max_xor(L,R)
print(f"Max xor value is {result}")