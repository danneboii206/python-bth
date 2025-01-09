#!/usr/bin/env python3

"""
bd5a5e58391a53c7f614213343a68b56
python
lab3
v4
daab24
2024-09-26 08:06:48
v4.0.0 (2019-03-05)

Generated 2024-09-26 10:06:48 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb
import functions


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 3 - python
#
# In this lab we take another look at functions and we use modules to
# structure our code.
#



# --------------------------------------------------------------------------
# Section 1. Functions
#
#
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create a function `valid_password` that takes one string argument. Check
# whether the argument is a valid password according to the following rules:
#
# * 8 characters or longer
# * Contains upper and lowercase letters
# * Contains a number
#
# The function should return True or False depending on whether the password
# is valid.
#
# Answer with the return value of the function when called with the string
# 'test'.
#
# Tip: Use built-in character functions `isupper()`, `islower()`,
# `isdigit()`.
#
# Write your code below and put the answer into the variable ANSWER.
#

def valid_password(password):
    '''
    Validating passwords
    '''
    digit = 0
    upper = 0
    lower = 0
    if len(password) >= 8:
        for char in password:
            if char.isdigit():
                digit += 1
            if char.isupper():
                upper += 1
            if char.islower():
                lower += 1
    else:
        return False
    test = (digit >= 1 and upper >= 1 and lower >= 1)
    return bool(test)

passcheck = valid_password("test")

ANSWER = passcheck

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Using the function `valid_password` answer with the return value of the
# function when called with the string 'anoth3ePw0Rd'.
#
# Write your code below and put the answer into the variable ANSWER.
#


passcheck = valid_password("anoth3ePw0Rd")



ANSWER = passcheck

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Create a function `number_of_vowels` that takes one argument. The function
# returns the number of vowels (vokaler) in the given argument. The following
# letters is used as vowels in this exercise: aeiouy. Your solution should be
# case-insensitive.
#
# Answer with the number of vowels in the following text:
#
# 'Stoicism has just a few central teachings. It sets out to remind us of how
# unpredictable the world can be.'
#
# Write your code below and put the answer into the variable ANSWER.
#

def number_of_vowels(inp):
    '''
    Returns the number of vowels
    '''
    num = 0
    vowels = "aeiouy"
    inp2 = inp.lower()
    for char in inp2:
        if char in vowels:
            num += 1
    return num

ans = number_of_vowels("Stoicism has just a few central teachings." 
                    +"It sets out to remind us of how unpredictable the world can be.")


ANSWER = ans

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Create a function `analyze_password` that uses `valid_password` and
# `number_of_vowels`. The function should return whether or not a password is
# valid and how many vowels the given password contains concatenated to a
# string.
#
# Example: With the input value Se3ret the function should return the
# following string: 'Se3ret is not a valid password and contains 2 vowels.'.
#
# Example: With the input value anoth3ePw0Rd the function should return the
# following string: 'anoth3ePw0Rd is a valid password and contains 3
# vowels.'.
#
# Answer with the return value of the function `analyze_password` called with
# the following argument: Se3ret.
#
# Write your code below and put the answer into the variable ANSWER.
#

def analyze_password(password):
    '''
    Analysing number of vowels and the validity of password
    '''
    num = number_of_vowels(password)
    valid = valid_password(password)
    res2 = ""
    if valid is True:
        res2 = (f"{password} is a valid password and contains {num} vowels.")
    else:
        res2 = (f"{password} is not a valid password and contains {num} vowels.")
    return res2


answer = analyze_password("Se3ret")




ANSWER = answer

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. Modules
#
# In this section we will look into modules and how we can structure our
# code.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Create a new Python file called `functions.py`. Import your new file/module
# in `answer.py` using the import statement: `import functions`
#
# In your new module, create a function called `multiplication` that takes
# two arguments. The function should return the product of the two arguments.
#
# Answer with the return value from a call to the function with the two
# arguments 51 and 42.
#
# Write your code below and put the answer into the variable ANSWER.
#

res = functions.multiplication(51, 42)



ANSWER = res

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# In your new module, create a function called `funny_word` that takes one
# argument and prepends it to the string ' is a funny word'. **EXAMPLE:** If
# the argument is 'water', the function should return: `"water is a funny
# word"`.
#
# Use the argument 'restaurant' and answer with a call to the function.
#
# Write your code below and put the answer into the variable ANSWER.
#

res = functions.funny_word("restaurant")




ANSWER = res

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (1 points)
#
# In your new module, create a function called `decider`. The function takes
# one argument. If the argument is a string return a call to `funny_word()`,
# if the argument is an integer return the square of the argument by using
# the `multiplication` function.
#
# Answer with a call to the function `decider` with the value `30` as
# argument.
#
# Write your code below and put the answer into the variable ANSWER.
#


res = functions.decider("30")



ANSWER = res

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.4 (1 points)
#
# In your new module, create a function called `double_decider`. The function
# takes two arguments. For each argument call the `decider` function.
# Concatenate the returned values in a string.
#
# Separate the two values by ' and the square is '.
#
# Answer with a call to the function `double_decider` with the values:
# 'hemidemisemiquaver' and 26 as arguments.
#
# Write your code below and put the answer into the variable ANSWER.
#


res = functions.doubledecider("hemidemisemiquaver", 26)


ANSWER = res

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.4", ANSWER, False)


dbwebb.exit_with_summary()
