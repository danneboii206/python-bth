#!/usr/bin/env python3

"""
9b617a883274e1c50ac1bb06ec70af20
python
lab6
v4
daab24
2024-10-23 18:00:02
v4.0.0 (2019-03-05)

Generated 2024-10-23 20:00:02 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 6 - python
#
# During these exercises we train on reading, writing and appending data to
# text file's.
#



# --------------------------------------------------------------------------
# Section 1. Files
#
#
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Read the `quotes.txt` -file in UTF-8 encoding and store the content into a
# variable. Answer with the number of characters in the file.
#
# Write your code below and put the answer into the variable ANSWER.
#

with open("quotes.txt", "r", encoding="UTF-8") as fhand:
    fhandr = fhand.read()
    lenfhand = len(fhandr)





ANSWER = lenfhand

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Use your variable from the exercise above and answer with the contents on
# line number 2. You should not have a newline at the end of the line.
#
# Write your code below and put the answer into the variable ANSWER.
#

splitlines = fhandr.splitlines()
line = splitlines[1]


ANSWER = line

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# First, read the content inside of quotes.txt and remove the 5 last rows.
# Then replace line number 6 with the new string "I am replaced".
# Then, create a new file called `newQuotes.txt` where you save the new
# changes. Replace `newQuotes.txt` if it already exists.
#
# Answer with the new content inside `newQuotes.txt`. Don't have a "\n" on
# the last line.
#
# Write your code below and put the answer into the variable ANSWER.
#

textlist = []

with open("quotes.txt", "r", encoding="UTF-8") as fhand:
    for line in fhand:
        textlist.append(line)
    textlist = textlist[:-5]
    textlist[5] = "I am replaced\n"

n = len(textlist) - 1
newstr = textlist[n]
newstr = newstr.replace("\n", "")
textlist[n] = newstr

with open("newQuotes.txt", "w", encoding="UTF-8") as fhandw:
    for element in textlist:
        fhandw.write(element)

with open("newQuotes.txt", "r+", encoding="UTF-8") as fhand2:
    content = fhand2.read()



ANSWER = content

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Append the following sentence on a new line at the end of newQuotes.txt and
# answer with the content.
#
# *"Luck is where preparation meets opportunity."*
#
# Write your code below and put the answer into the variable ANSWER.
#


with open("newQuotes.txt", "a", encoding="UTF-8") as fhand:
    fhand.write("\n" + "Luck is where preparation meets opportunity.")

with open("newQuotes.txt", "r", encoding="UTF-8") as fhand:
    content = fhand.read()


ANSWER = content

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Store the number of empty lines that `passwords.txt` has and create a new
# file called `newPasswords.txt` containing the lines that are not empty.
#
# Answer with the following:
#
# *passwords.txt has X empty lines and contains: Y*
#
# Replace `X` with the number of empty lines and `Y` with the new files
# content.
#
# Write your code below and put the answer into the variable ANSWER.
#
wspaces = 0
listres = []
with open("passwords.txt", "r", encoding="UTF-8") as fhand:
    for line in fhand:
        if line == "\n":
            wspaces += 1
        else:
            listres.append(line)


with open("newPasswords.txt", "w", encoding="UTF-8") as fhandw:
    for element in listres:
        fhandw.write(element)

with open("newPasswords.txt", "r", encoding="UTF-8") as fhandr:
    content = fhandr.read()

res = f"passwords.txt has {wspaces} empty lines and contains: {content}"

ANSWER = res

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, True)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6 (3 points)
#
# Write the content of line numbers 2, 3 and 4 from `quotes.txt` to a new
# file that you create called `extraQuotes.txt`. Replace `extraQuotes.txt` if
# it already exists.
# Save the total number of characters and the 9 first characters of the
# second line into variables.
#
# Answer with the following string:
# "The file has X characters and the 9 first of the second row are: Y"
#
# **Example**:
# *"The file has 220 characters and the 9 first of the second row are: - Jon
# Doe"*
#
# Do not include newlines when you count the number of characters.
#
# Write your code below and put the answer into the variable ANSWER.
#


ANSWER = "Replace this text with the variable holding the answer."

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.6", ANSWER, False)


dbwebb.exit_with_summary()
