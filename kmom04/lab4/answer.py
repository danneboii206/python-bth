#!/usr/bin/env python3

"""
de19b0ec2690573cd3fd83b926bd4f93
python
lab4
v4
daab24
2024-10-01 17:54:43
v4.0.0 (2019-03-05)

Generated 2024-10-01 19:54:43 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 4 - python
#
# "In these exercises we will take a look into lists."
#



# --------------------------------------------------------------------------
# Section 1. List basics
#
#
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Concatenate the two lists [bobcat, Whitaker] and [Berenger, flute].
#
# Answer with your list.
#
# Write your code below and put the answer into the variable ANSWER.
#


tot_list = ["bobcat", "Whitaker"] + ["Berenger", "flute"]



ANSWER = tot_list

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Use the list [lion, tiger, ozelot, bobcat, cougar].
#
# Add the words 'hotdog' and 'jacket' as the second and third element.
#
# Answer with the modified list.
#
# Write your code below and put the answer into the variable ANSWER.
#


tot_list = ["lion", "tiger", "ozelot", "bobcat", "cougar"]
tot_list.insert(1, "hotdog")
tot_list.insert(2, "jacket")



ANSWER = tot_list

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Use the list [lion, tiger, ozelot, bobcat, cougar].
#
# Replace the third word with: 'potato'.
#
# Answer with the modified list.
#
# Write your code below and put the answer into the variable ANSWER.
#

tot_list = ["lion","tiger","ozelot","bobcat","cougar"]
tot_list[2] = "potato"


ANSWER = tot_list

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Sort the list
#
# > [wasp, fly, butterfly, bumblebee, mosquito]
#
# in descending alphabetical order. Answer with the sorted list.
#
# Write your code below and put the answer into the variable ANSWER.
#


tot_list = ["wasp","fly","butterfly","bumblebee","mosquito"]
tot_list.sort(reverse = True)



ANSWER = tot_list

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Use `remove()` to delete the word:
#
# > 'floor'
#
# from the list:
#
# > [table, wall, desk, chair, floor]
#
# Answer with the modified list.
#
# Write your code below and put the answer into the variable ANSWER.
#


tot_list = ["table","wall","desk","chair","floor"]
tot_list.remove("floor")



ANSWER = tot_list

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. Built-in list functions
#
# Some basic built-in functions.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Use a built-in function to sum all numbers in the list:
#
# > [45, 22, 2, 498, 78]
#
# Answer with the result as an integer.
#
# Write your code below and put the answer into the variable ANSWER.
#

tot_list = [45,22,2,498,78]
total = sum(tot_list)




ANSWER = total

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# Use built-in functions, such as `sum` and `len` to get the average value of
# the list:
#
# > [123, 4, 125, 69, 155]
#
# Answer with the result as a float with at most one decimal.
#
# Write your code below and put the answer into the variable ANSWER.
#

tot_list = [123,4,125,69,155]
avg = float(sum(tot_list) / len(tot_list))
avg_rounded = round(avg,1)



ANSWER = avg_rounded

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (1 points)
#
# Use the built-in functions `split()` and `join()` to fix this string:
#
# > "The?snow?is?falling"
#
# into a real sentence, (without '?').
#
# Answer with the fixed string.
#
# Write your code below and put the answer into the variable ANSWER.
#


strg = "The?snow?is?falling"
a = strg.split("?")
b = " ".join(a)


ANSWER = b

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.4 (1 points)
#
# Use slice on the list
#
# > [tree, stone, grass, water, sky]
#
# and replace the second and third elements with the elements in the
# following list.
#
# > "green, purple"
#
# Answer with the modified list.
#
# Write your code below and put the answer into the variable ANSWER.
#

tot_list = ["tree","stone","grass","water","sky"]
slice1 = slice(0, 1)
slice2 = slice(3, 5)
new_list = tot_list[slice1]
new_list.insert(1, "green")
new_list.insert(2, "purple")
new_list = new_list + tot_list[slice2]



ANSWER = new_list

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.4", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.5 (1 points)
#
# Assign the list
#
# > [b, a, e, d, c]
#
# to a variable called 'list1'.
#
# Assign the list again, but to another variable called 'list2'.
#
# Answer with the result of 'list1 is list2'.
#
# Write your code below and put the answer into the variable ANSWER.
#

list1 = ["b", "a", "e", "d", "c"]
list2 = ["b", "a", "e", "d", "c"]

a = list1 is list2



ANSWER = a

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.6 (1 points)
#
# Use your lists from the last exercise. Assign 'list1' to another variable
# called 'list3' like this:
#
# > list3 = list1
#
# Answer with the result of 'list1 is list3'.
#
# Write your code below and put the answer into the variable ANSWER.
#

list3 = list1

a = list3 is list1




ANSWER = a

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.6", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.7 (1 points)
#
# Use your lists from the last exercise. Change the first element in 'list1'
# to
#
# > "s"
#
# Answer with 'list3'.
#
# Write your code below and put the answer into the variable ANSWER.
#

list1[0] = "s"




ANSWER = list3

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.7", ANSWER, True)

# --------------------------------------------------------------------------
# Section 3. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.1 (3 points)
#
# Create a function that returns the list passed as argument sorted in
# numerical and ascending order. Also multiply all values with 10.
#
# Use the list:
#
# > [98, 5, 12, 369, 1]
#
# and the built-in method `sort()`.
#
# Answer with the sorted list.
#
# Write your code below and put the answer into the variable ANSWER.
#


def sorter(lizt):
    '''
    Multiplying every element in list by 10 and sorting the list
    in numerical order
    '''
    i = 0
    lizt.sort()
    for num in lizt:
        num = num * 10
        lizt[i] = num
        i += 1
    return lizt

list1 = [98, 5, 12, 369, 1]


a = sorter(list1)



ANSWER = a

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.2 (3 points)
#
# Create a function that takes the list:
#
# > [123, 4, 125, 69, 155]
#
# as argument.
#
# The function should multiply all even numbers by 3 and add 8 to all odd
# numbers.
#
# Answer with the modified list sorted in numerical order, descending.
#
# Write your code below and put the answer into the variable ANSWER.
#




def evenornot(lizt):
    '''
    Multiplies by 3 if even, adds by 8 if not
    '''
    i = 0
    for num in lizt:
        if num % 2 == 0:
            num = num * 3
            lizt[i] = num
            i += 1
        else:
            num = num + 8
            lizt[i] = num
            i += 1
    lizt.sort(reverse = True)
    return lizt

list1 = [123, 4, 125, 69, 155]

a = evenornot(list1)


ANSWER = a

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.2", ANSWER, True)


dbwebb.exit_with_summary()
