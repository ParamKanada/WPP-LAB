'''2. Write a program that generates 100 random integers that are either 0 or 1. Then find the
longest run of zeros, the largest number of zeros in a row. For instance, the longest run of
zeros in [1,0,1,1,0,0,0,0,1,0,0] is 4.'''

import random

#geneate 100 intgers that are 1 or 0
random_numbers = [random.randint(0, 1) for _ in range(100)] #makes a list of 0 and 1

# Find the longest run of zeros
longest_run = 0
current_run = 0

for number in random_numbers:
    if number == 0:
        current_run += 1
        if current_run > longest_run:
            longest_run = current_run
    else:
        current_run = 0 #it's like reseting a streak

#output
print("Random numbers:", random_numbers)
print("Longest run of zeros:", longest_run)