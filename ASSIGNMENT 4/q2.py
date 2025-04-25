import math
def intSqures(a,b):
    count=0
    for i in range(a,b+1):
        if math.sqrt(i)-int(math.sqrt(i)) ==0:
            count+=1
    return count

t = int(input("Enter the number of test cases: "))
for i in range(t):
    st = input("Enter a and b: ")
    nums=st.split()
    count=intSqures(int(nums[0]),int(nums[1]))
    print(count)