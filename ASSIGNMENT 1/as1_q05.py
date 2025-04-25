'''5. You are a student in a class of 10. Your class teacher assigns you a task of entering the
names of all the students in the class. You finally want to display the names given the
condition that the maximum allowed characters in a name is 15. As a fun task, reverse the
names and display them. [Hint: Slicing works when you are selecting maximum characters]'''

#making a list of all names that user inputs
all_names = []
for i in range(3):
    name = input(f"Enter name of student {i+1}")
    all_names.append(name)

#now all_names is a list containing all the names
for name in all_names:
    ls = list(name)
    for i in range(1,len(ls)+1):    #printing using nrgative index
        print(ls[-i],sep="",end="")
    print()