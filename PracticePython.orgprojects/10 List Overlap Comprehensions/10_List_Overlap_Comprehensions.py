#Exercise 10 (and Solution)
#This week’s exercise is going to be revisiting an old exercise (see Exercise 5), except require the solution in a different way.

#Take two lists, say for example these two:

#	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes. Write this in one line of Python using at least one list comprehension. (Hint: Remember list comprehensions from Exercise 7).

#The original formulation of this exercise said to write the solution using one line of Python, but a few readers pointed out that this was impossible to do without using sets that I had not yet discussed on the blog, so you can either choose to use the original directive and read about the set command in Python 3.3, or try to implement this on your own and use at least one list comprehension in the solution.

#Extra:

#Randomly generate two lists to test this


import random
list_1 = []
list_2 = []


# Creating a list of random elements(10 to 50), and random numbers (1 to 100)
#Why two for loops? Simple. if I run just 1 random (1-20) loop, both lists will get the same amount of elements, I'm looking for a random scenario like the cases from the excercise lists a and b, I want to reproduce it exactly that way.
# So different sized lists with randomized numbers! Loop Away! :) 
for i in range(random.randint(10,51)):
    rando_num1 = random.randint(1,101)
    list_1.append(rando_num1)
    
for j in range(random.randint(10,51)):
    rando_num2 = random.randint(1,101)
    list_2.append(rando_num2)

#just printing to check if everything is alright..
print('List 1: ', list_1)
print('List 2: ', list_2)

#So far so good!
#Iniztializing an empty list for the common value appending

append_me_common = []

for k in list_1:
    for z in list_2:
        if k==z :
            append_me_common.append(k)
        else:
            pass
print('Your new list with common items is...')
print('\n')
print('Common List : ', append_me_common)
