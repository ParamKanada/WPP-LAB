def max_pieces(n):
    max_cuts=0
    if n%2==0:
        return (n//2 + 1)*(n//2 +1)
    if n%2==1:
        return (n//2 + 1)*((n+1)//2 + 1)
    
k=int(input("Enter number 0f cuts: "))
print(f"Maximum number of pieces are:{max_pieces(k)}")