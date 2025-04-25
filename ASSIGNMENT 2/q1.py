# Q1. Write a program that asks the user to enter a word and then capitalizes every other letter of
# that word. So, if the user enters rhinoceros, the program should print rHiNoCeRoS.


def capitalize_even(word):
    new_word = ""
    for i in range(len(word)):
        if i % 2 == 1:  # Even index but odd position
            new_word+=word[i].upper()   #i will access individual letters of given string through this and then add to new string
        else:  # Odd index but even position
            new_word+=word[i].lower()
    return new_word

word = input("Enter a word: ")
new_word = capitalize_even(word)
print(new_word)