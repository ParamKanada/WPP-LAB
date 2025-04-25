def isPangram(str):
    count=0
    str=str.lower()
    str=list(str)
    for i in range(97,122+1):
        if chr(i) in str:
            count+=1
            continue
    if count==26:
        print(f"{str} is pangram")
    else:
        print("Not pangram")

st = input("Enter the string")
isPangram(st)