'''
Different modules and functions for main.py
'''
import marvin2

def greet():
    '''
    Greets the user
    '''
    name = input("What is your name? ")
    print("Lucy says:\n")
    print(f"Hello {name} - wassaaaap?")
    print("What do you desire?")

def celsius_to_fahrenheit():
    '''
    Converts from celsius to fahrenheit
    '''
    print("Lucy says:\n")
    celsius = float(input("Write the degrees in fahrenheit "))
    # Fahrenheit formula ((C° x 9/5) + 32)
    fahrenheit = round((celsius * 9/5 + 32), 2)
    print(f"The requested temperature is {fahrenheit} °F")
    print("A whole lot colder than hell...")

def points_to_grade():
    '''
    Calculating the grade from a given max score
    '''
    maxpoints = int(input("How many points were there to earn: "))
    points = int(input("How many points did you earn: "))
    percent = float(points / maxpoints)
    if percent >= 0.9:
        grade = "A"
    elif 0.8 <= percent < 0.9:
        grade = "B"
    elif 0.7 <= percent < 0.8:
        grade = "C"
    elif 0.6 <= percent < 0.7:
        grade = "D"
    else:
        grade = "F"
    print(f"score: {grade}")

def sum_and_average():
    '''
    Printing out the sum and average for inserted numbers
    '''
    count = 0
    total = 0
    #loop the calculations
    while True:
        inp = input("Write a number (or done to exit): ")
        if inp in ("Done", "done"): #breaks incase the input is done, exits
            break                   #the for-loop
        number = float(inp)
        #the actual calculations
        total = total + number
        count = count + 1
        average = round(total / count, 2)
    print(f"The total sum is {total} and the avereage is {average}")

def hyphen_string():
    '''
    Adding hyphens between chars in a string
    '''
    text = input("Write anything u want\n")
    len_text = len(text)
    result_text = ""
    i = 0
    while i != len_text:
        result_text += text[0 + i] * (i + 1)
        i = i + 1
        if i != (len_text):
            result_text += "-"
    print(result_text)

def compare_numbers():
    '''
    Comparing if the last inserted number is smaller or larger than new numbers
    '''
    nmr = 0
    i = 0
    old_nmr = 0
    while True:
        inp = input("Write a number or done: ")
        if inp in ("Done", "done"):
            break
        try:
            nmr = float(inp)
        except(ValueError):
            print("not a number!")
            continue
        if i < 1:
            old_nmr = nmr
            i = i + 1
            continue
        if nmr < old_nmr:
            print("smaller!")
        if nmr > old_nmr:
            print("larger!")
        if nmr == old_nmr:
            print("same!")
        old_nmr = nmr

def validate_ssn():
    '''
    Validates the SSN
    '''
    total = marvin2.calculate_luhna_sum(input("Enter ssn \n >>> "))
    total_str = str(total)
    no_hyphen = total_str.replace("-","")
    total_len = len(no_hyphen)
    if total % 10 == 0 and total_len < 10:
        print("Valid")
    else:
        print("Not valid")

def robber_language():
    '''
    Converts plain text to the swedish robber language.
    '''
    consonants = "aeiouyåäö"
    ans = ""
    inp = input("Write a message to convert to robber language: ")
    for char in inp.lower():
        if char in consonants:
            ans += str(char)
        else:
            ans += str(char) + "o" + str(char)
    print(ans)
