#implementing replace function

st = input("Enter String:\t")
st_1 = input("To replace=\t")
st_2 = input("To replace with=\t")

result=""

for i in range(len(st)):
    if st[i:len(st_1)+1:1] == st_1:
        
print(st)