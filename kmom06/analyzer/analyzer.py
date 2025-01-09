'''
Functions for main.py
'''

from operator import itemgetter

def openfile(fname):
    '''
    opening text file & inserting contents into string
    '''
    with open(fname, encoding ="utf-8")  as fhand:
        lines = fhand.read()
    return lines

def make_to_list(lines):
    '''
    making .txt file to list
    '''
    word_list = lines.split("\n")
    return word_list

def check_lines(fname):
    '''
    checking lines in list
    '''
    lines = openfile(fname)
    word_list = make_to_list(lines)
    l_am = len(word_list)
    return l_am

def remove_all_non_letters(lines):
    '''
    Remove non-letters from lines
    '''
    line1 = lines.replace(".", "")
    line2 = line1.replace(",", "")
    line3 = line2.replace("-", "")
    return line3


def check_words(fname):
    '''
    checking words in list
    '''
    lines = openfile(fname)
    word_list = make_to_list(lines)
    count = 0
    for element in word_list:
        temp_list = element.split(" ")
        count += len(temp_list)
    return count


def check_letters(fname):
    '''
    checking letters in list
    '''
    lines = openfile(fname)
    new_lines = remove_all_non_letters(lines)
    word_list = make_to_list(new_lines)
    count = 0
    for element in word_list:
        for letter in element:
            if letter != " ":
                count += 1

    return count

def item_lister(listname):
    '''
    making lists out of elements which includes the element and how often it appears
    reference: https://www.geeksforgeeks.org/python-frequency-of-each-character-in-string/
    '''
    w_freq = {}
    for element in listname:
        temp_list = element.split(" ")
        for keys in temp_list:
            w_freq[keys] = w_freq.get(keys, 0) + 1 #from ref
    return w_freq

def percent_checker(listname, num_count):
    '''
    Checking how often an element comes up
    '''
    percent_list = []
    for nums in listname:
        temp_str = f"{round(((nums/num_count) * 100), 1)}%"
        percent_list.append(temp_str)
    return percent_list

def sorter(freqlist):
    '''
    Sorting dicts by value & letter
    '''
    sorted_values = sorted(freqlist.values(), reverse=True)
    sorted_keys = sorted(freqlist.items(), key=itemgetter(1, 0), reverse=True)
    return sorted_values, sorted_keys

def word_frequency(fname):
    '''
    checking the most used words in file
    reference: https://www.geeksforgeeks.org/python-frequency-of-each-character-in-string/
    '''
    lines = openfile(fname).lower()
    newlines = remove_all_non_letters(lines)
    word_list = make_to_list(newlines)
    w_freq = item_lister(word_list)
    num_count = check_words(fname)
    sorted_values, sorted_keys = sorter(w_freq)
    percent_list = percent_checker(sorted_values, num_count)
    top7_words = sorted_keys[:7]
    top7_percent = percent_list[:7]
    i = 0
    ret_str = ""
    for word, number in top7_words:
        ret_str += (f"{word}: {number} | {top7_percent[i]} \n")
        i += 1
    return ret_str

def letter_list_creater(lines):
    '''
    Creating the letter list
    '''
    letter_list = []
    for letter in lines:
        if letter not in ("\n", " "):
            letter_list.append(letter)
    return letter_list


def letter_frequency(fname):
    '''
    Checking how often a letter comes up in file
    '''
    lines = openfile(fname).lower()
    newlines = remove_all_non_letters(lines)
    letter_list = letter_list_creater(newlines)
    num_count = check_letters(fname)
    l_freq = item_lister(letter_list)
    sorted_values, sorted_keys = sorter(l_freq)
    percent_list = percent_checker(sorted_values, num_count)
    top7_letter = sorted_keys[:7]
    top7_percent = percent_list[:7]
    ret_str = ""
    i = 0
    for word, number in top7_letter:
        ret_str += (f"{word}: {number} | {top7_percent[i]} \n")
        i += 1
    return ret_str
