'''4. Take numbers from 1 to 10000. Create equivalence classes for modulo 5 on this set of
numbers. Check the validity of your equivalence classes. [Hint: the union of all equivalence
classes should be the original set/list.]'''

num_list = [i for i in range(1,10001)]
print(num_list)
union_class = []


#this is what i think quwstion means
class_1 = [num for num in num_list if num%5==1] #leaves reminder 1
class_2 = [num for num in num_list if num%5==2] #leaves reminder 2
class_3 = [num for num in num_list if num%5==3] #leaves reminder 3
class_4 = [num for num in num_list if num%5==4] #leaves reminder 4
class_5 = [num for num in num_list if num%5==0] #leaves reminder 0

union_class = class_1 + class_2 + class_3 + class_4 + class_5

if set(union_class) == set(num_list):
    print("Valid class")
else:
    print("Not valid")