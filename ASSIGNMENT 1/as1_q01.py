'''1. Create the following lists using a for loop.
(a) A list consisting of the integers 0 through 49
(b) A list containing the squares of the integers 1 through 50.
(c) The list ['a','bb','ccc','dddd', ...] that ends with 26 copies of the letter z.'''

list = []   #for (a)
sq_list = []    #for (b)
letter_list = []    #for (c)


for i in range(0,50):
 list.append(i)
 sq_list.append(i*i)

for i in range(0,26):
 letter_list.append(chr(i+65)*(i+1))

print(list)
print(sq_list)
print(letter_list)