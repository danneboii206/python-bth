#!/usr/bin/env python3

"""
7d1d1beae12c344bd30cfd7a963fc9cb
python
lab2
v4
daab24
2024-09-11 12:13:13
v4.0.0 (2019-03-05)

Generated 2024-09-11 14:13:13 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb

# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 2 - python
#
# In this exercise we will look into flow-control. If-statements, for-loops
# and while-loops.
#



# --------------------------------------------------------------------------
# Section 1. Boolean operators and if-statements
#
# The basics of boolean operators and if-statements.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create three variables representing dice values: `dice1` = 1, `dice2` = 5
# and `dice3` = 2.
#
# Answer with the boolean value of the expression '`dice1` is greater than
# `dice2`'.
#
# Write your code below and put the answer into the variable ANSWER.
#


dice1 = 1
dice2 = 5
dice3 = 2

check = dice1 > dice2



ANSWER = check

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Sum the three variables `dice1`, `dice2` and `dice3`.
#
# Use an if-statement to decide if the sum of the three variables i greater
# than 11. If the sum is greater than 11 answer with 'big' otherwise answer
# with 'small'.
#
# Write your code below and put the answer into the variable ANSWER.
#


sum_dice = dice1 + dice2 + dice3
ans = ""

if sum_dice >= 11:
    ans = "big"
else:
    ans = "small"



ANSWER = ans

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Add the sum of `dice4` = 2 and `dice5` = 1 to the sum of the three other
# dices.
#
# Use an if, elseif, else statement to check the total value of the dices.
# Answer with 'small' if the sum is smaller than 11, 'intermediate' if the
# sum is greater than or equal to 11 but smaller than 21. If the sum is
# greater than or equal to 21 answer with 'big'.
#
# Write your code below and put the answer into the variable ANSWER.
#

dice4 = 2
dice5 = 1

sum2_dice = sum_dice + dice4 + dice5

if sum2_dice < 11:
    ans = "small"
elif sum2_dice >= 11:
    ans = "intermediate"
else:
    ans = "big"

ANSWER = ans

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Create a variable `summer_word` containing the word 'beach'.
#
# Answer with True if `summer_word` contains the letter 's' otherwise answer
# with False.
#
# Tip: Use the `in` operator.
#
# Write your code below and put the answer into the variable ANSWER.
#


summer_word = "beach"


if "s" in summer_word:
    check = True
else:
    check = False



ANSWER = check

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. For-loops
#
# The basics of iteration and for-loops.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Loop through the numbers 0 to 10 (10 included) and concatenate a string
# with the numbers comma-separated. You should have a comma at the end of the
# string.
#
# Answer with the string.
#
# Write your code below and put the answer into the variable ANSWER.
#

count = ""

for i in range(11):
    count += (str(i) + ",")





ANSWER = count

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# Loop through the letters of the variable `summer_word` from above.
# Concatenate the consonants from `summer_word` and answer with the new word.
#
# Tip: Create a string that contains consonants and check if each letter is
# in it.
#
# Write your code below and put the answer into the variable ANSWER.
#

consonants = "bcdfghjklmnpqrstvwxyz"
ans = ""

for char in summer_word:
    if char in consonants:
        ans += str(char)


ANSWER = ans

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (1 points)
#
# Loop through all numbers from 50 to 84 both numbers included. Add all odd
# (udda) numbers together and answer with the result.
#
# Tip: Use the modulus % operator.
#
# Write your code below and put the answer into the variable ANSWER.
#

sum_num = 0

for i in range(50,85):
    if i % 2:
        sum_num += i

ANSWER = sum_num

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, True)

# --------------------------------------------------------------------------
# Section 3. While-loops
#
# The basics of while-loops.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.1 (1 points)
#
# Create a while-loop that starts at value 6 and ends when the value is
# greater than 61, the value should be incremented by 3 for each iteration.
# Concatenate a string with the values comma-separated. You should have a
# comma at the end of the string.
#
# Answer with the string.
#
# Write your code below and put the answer into the variable ANSWER.
#

x = 6
res = ""

while x <= 61:
    if x == 63:
        break
    res = res + str(x) + ","
    x = x + 3

ANSWER = res

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.1", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.2 (1 points)
#
# Create a while-loop that subtracts 7 from 59, 21 times. Answer with the
# result.
#
# Write your code below and put the answer into the variable ANSWER.
#

x = 21
y = 59

while x != 0:
    y = y - 7
    x = x - 1




ANSWER = y

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.3 (1 points)
#
# Create a while-loop that calculates the factorial number for 5, 5!. The
# factorial of a number is the number multiplied by all smaller integers
# greater than 1. The factorial of 5 is `5 * 4 * 3 * 2 * 1`. Answer with the
# result.
#
# Write your code below and put the answer into the variable ANSWER.
#

x = 5
y = 1

while x != 0:
    y = y * x
    x = x - 1







ANSWER = y

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.3", ANSWER, False)

# --------------------------------------------------------------------------
# Section 4. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 4.1 (3 points)
#
# Use a for-loop or a while-loop to reverse the word 'disproportionality'.
#
# Answer with the reversed word.
#
# Write your code below and put the answer into the variable ANSWER.
#

disp = "disproportionality"
length = len(disp)
rev_disp = ""
i = 0

while i < length:
    rev_disp += disp[-1 - i]
    i = i + 1



ANSWER = rev_disp

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("4.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 4.2 (3 points)
#
# Swedish numberplates consist of three letters and three numbers (Not using
# new plates which can have more letters). The numbers range from 001 to 999.
# Using one of the four common rules of arithmetics (+, -, *, /), on how many
# of the numberplates can the two first numbers give the third number? We
# only care about the numbers, we ignore letters for this assignment.
#
# Alternatives:
# a + b = c
# a - b = c
# a * b = c
# a / b = c
#
# Do not count multiple times if more than one rule of arithmetics work.
#
# Examples:
# '123' can be combined to 1 + 2 = 3. So this numberplate is good. Since this
# matched on + operator, we don't continue checking with the other operators.
# '129' 1 and 2 cannot be combined to give 9 using the four rules of
# arithmetics, so this does not work.
#
#
# Answer with the number of numberplates.
#
# Write your code below and put the answer into the variable ANSWER.
#

ANSWER = ""

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("4.2", ANSWER, True)


dbwebb.exit_with_summary()
