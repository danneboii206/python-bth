#!/usr/bin/env python3

"""
b2245ec63b713840875dacceb33e20ee
python
lab5
v4
daab24
2024-10-10 07:21:33
v4.0.0 (2019-03-05)

Generated 2024-10-10 09:21:33 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 5 - python
#
# A look into dictionaries and tuples.
#



# --------------------------------------------------------------------------
# Section 1. Dictionaries
#
# Some basics with dictionaries.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create a small phonebook using a dictionary. Use the names as keys and
# numbers as values.
#
# Use
#
# > Ross, Chandler, Monica
#
# and corresponding numbers
#
# > 55523645, 55564452, 55545872
#
# Add the phonenumbers as integers. Answer with the resulting dictionary.
#
# Write your code below and put the answer into the variable ANSWER.
#

phonebook = {
    "Ross" : 55523645,
    "Chandler" : 55564452,
    "Monica" : 55545872
}







ANSWER = phonebook

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# How many items are there in the phonebook dictionary?
#
# Write your code below and put the answer into the variable ANSWER.
#

lenpb = len(phonebook)




ANSWER = lenpb

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Use the `get()` method on your phonebook and answer with the phonenumber of
# 'Monica'.
#
# Write your code below and put the answer into the variable ANSWER.
#

monnum = phonebook.get("Monica")




ANSWER = monnum

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Get all keys from the phonebook dictionary and return them in a sorted
# list.
#
# Write your code below and put the answer into the variable ANSWER.
#


pbsorted = sorted(phonebook)



ANSWER = pbsorted

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Get all values from the phonebook dictionary and return them in a sorted
# list.
#
# Write your code below and put the answer into the variable ANSWER.
#


pbnumsorted = sorted(phonebook.values())



ANSWER = pbnumsorted

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6 (1 points)
#
# Use the in-operator to test if the name 'Monica' exists in the phonebook
# dictionary. Answer with the return boolean value.
#
# Write your code below and put the answer into the variable ANSWER.
#


check = "Monica" in phonebook



ANSWER = check

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.6", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.7 (1 points)
#
# Create a copy of the phonebook dictionary.
# Get and remove the item 'Monica' from the copied phonebook (use pop()).
# Answer with the resulting dictionary.
#
# Write your code below and put the answer into the variable ANSWER.
#


phonebook_2 = phonebook

phonebook_2.pop("Monica")



ANSWER = phonebook_2

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.7", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. Tuples
#
# Some basics with tuples.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Create a tuple with 'bear, 65, 6.47, chair, 5'. Answer with the length of
# the tuple as an integer.
#
# Write your code below and put the answer into the variable ANSWER.
#


tup = ("bear", 65, 6.47, "chair", 5)
tuplen = len(tup)


ANSWER = tuplen

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# Create a tuple out of:
#
# > (bear, 65, 6.47, chair, 5).
#
# Assign each value in the tuple to different variables:
#
# > 'a','b','c','d','e'.
#
# Answer with the variable: 'd'.
#
# Write your code below and put the answer into the variable ANSWER.
#

a = tup[0]
b = tup[1]
c = tup[2]
d = tup[3]
e = tup[4]




ANSWER = d

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (1 points)
#
# Use the list
#
# > [123, 4, 125, 69, 155]
#
# Assign the first two elements to a tuple with a slice on the list.
#
# Answer with the first element in the tuple as an integer.
#
# Write your code below and put the answer into the variable ANSWER.
#

numlist = [123, 4, 125, 69, 155]

x = slice(2)

slicedlist = numlist[x]

tup = tuple(slicedlist)

newint = int(tup[0])

ANSWER = newint

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.4 (1 points)
#
# Create a tuple with
#
# > (45, 22, 2, 498, 78)
#
# Convert it to a list and replace the second element with:
#
# > 1918
#
# Convert it back to a tuple and answer with the first three elements in a
# comma-separated string,  without an ending `,`.
#
# Write your code below and put the answer into the variable ANSWER.
#

tup = (45, 22, 2, 498, 78)
numlist = []

for numb in tup:
    numlist.append(numb)

numlist[1] = 1918
tup2 = tuple(numlist)

numstr = ""
counter = 0

for numb in tup2:
    if counter == 3:
        break
    if counter != 2:
        numstr += str(numb) + ","
    else:
        numstr += str(numb)
    counter += 1


ANSWER = numstr

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.4", ANSWER, True)

# --------------------------------------------------------------------------
# Section 3. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.1 (3 points)
#
# Use a for-loop to walk through the original phonebook dictionary and create
# a string representing it. Each name and number should be on its own row,
# separated by a space. The names must come in alphabetical order. Note that
# every row should end with a newline character, `\n`.
#
# Answer with the resulting string.
#
# Write your code below and put the answer into the variable ANSWER.
#


ANSWER = "Replace this text with the variable holding the answer."

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.2 (3 points)
#
# Convert the phonenumber to a string and add the prefix '+1-', representing
# the language code, to each phone-number.
#
# Answer with the resulting dictionary.
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER = "Replace this text with the variable holding the answer."

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.2", ANSWER, False)


dbwebb.exit_with_summary()
