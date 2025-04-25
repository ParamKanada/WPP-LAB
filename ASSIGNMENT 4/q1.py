def palindrome(str):
    count = 0
    s=list(str)
    n=len(s)

    for i in range(n//2):
        left,right = s[i] , s[n-1-i]

        while left != right:
            if left > right:
                s[i]=chr(ord(s[i])-1)
            elif left < right:
                s[n-1-i]=chr(ord(s[n-1-i])-1)
            count+=1
            left, right = s[i], s[n - 1 - i]

    return count

count = palindrome("abd")
print(count)