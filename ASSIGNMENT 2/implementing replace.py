#implementing replace function

st = list(input("Enter String:\t"))
a = input("Enter the word to replace:\t")
b = input("Enter the word to replace it with:\t")
for i in range(len(st)):
    if st[i] == a:
        st[i]=b

print(str(st))