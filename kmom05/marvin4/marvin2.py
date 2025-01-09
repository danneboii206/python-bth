'''
New set of functions for main.py
'''

import random

def calculate_luhna_sum(text):
    '''
    Luhnalalgorithm to help in the creation of a ssn
    '''
    total = 0
    i = 2
    for number in text:
        if number == "-":
            continue
        if i % 2 == 0:
            ind_num = int(number) * 2
            if ind_num > 9:
                for num in str(ind_num):
                    total += int(num)
            else:
                total += (int(number) * 2)
        else:
            total += int(number)
        i += 1
    return total

def create_ssn(text):
    '''
    Creates a SSN according to the birthdate
    '''
    while True:
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
        num3 = random.randint(0, 9)
        total = (str(text) + "-" + str(num1) + str(num2) + str(num3))
        result_luhnal = calculate_luhna_sum(total)
        if result_luhnal % 10 == 0:
            continue
        nearest_ten = ((result_luhnal // 10) + 1) * 10
        num4 = nearest_ten - result_luhnal
        total += str(num4)
        return total

def get_acronym(text):
    '''
    Splits uppercase letter from lowercase to get acronyms
    '''
    result = ""
    for char in text:
        if char.isupper():
            result = result + char
    return result

#första tanken var en for loop men använder inte t.ex char någonstans
#använder while true pga pylint, kan inte komma vidare annars
def randomize_string(text):
    '''
    Scrambles the order of letters
    '''
    string = ""
    len_text = len(text)
    counter = 0
    while True:
        res = string.join(random.sample(text, len_text))
        counter += 1                                     
        if counter == len_text:
            break
    return res

def find_all_indexes(text, var):
    '''
    Find the positions of indexes inside a string
    '''
    num = 0
    i = 1
    res = ""
    while True:
        try:
            ans = text.index(var, num)
            if i == 1:
                res += str(ans)
            else:
                res += "," + str(ans)
            num = ans + 1
            i += 1
        except ValueError:
            break
    return res
