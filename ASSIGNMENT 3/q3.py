'''3. Utopian Tree
The Utopian tree goes through 2 cycles of growth every year. The first growth cycle occurs during the
monsoon, when it doubles in height. The second growth cycle occurs during the summer, when its height
increases by 1 meter.
Now, a new Utopian tree sapling is planted at the onset of the monsoon. Its height is 1 meter. Can you find
the height of the tree after N growth cycles?
Input Format
The first line contains an integer, T, the number of test cases.
T lines follow. Each line contains an integer, N, that denotes the number of cycles for that test case.
Constraints
1 <= T <= 10
0 <= N <= 60
Output Format
For each test case, print the height of the Utopian tree after N cycles.'''

def growth(n):
    height = 1  #initial height when planted
    for i in range (1,n+1):
        if i%2==1:
            height*=2
        else:
            height+=1
    return height

t=int(input("Enter number of test cases: "))
for _ in range(t):
    n = int(input("Enter number of growth cycles: "))
    print(f"Height after {n} cycles is: {growth(n)} meters")