'''
Checking the words and letters for the program
'''

import time
import random
import filehandler as fh

def sort_key(item):
    '''
    Custom key
    '''
    amount = item[1]
    letter = item[0].lower()
    return (amount, letter)

def word_length_checker(word_list):
    '''
    Checking the length of a word_list
    '''
    counter = i = 0 #iterations with different uses
    loop_am = len(word_list)
    while i < loop_am:
        list_of = word_list[i].split(" ")
        for _ in list_of:
            counter +=1
        i += 1
    return counter

def letter_length_checker(word_list):
    '''
    Checking how many letters are in the list
    '''
    counter = 0
    for word in word_list:
        for letter in word:
            if letter != " ":
                counter += 1
    return counter

def word_checker(temp_list_word, inp_list):
    '''
    Checking how many words are in the list
    '''
    extra_words = len(inp_list) - len(temp_list_word)
    i, wrong_am_word = 0, 0
    while i < len(temp_list_word):
        try:
            if temp_list_word[i] != inp_list[i]:
                wrong_am_word += 1
        except IndexError:
            pass
        i += 1
    return wrong_am_word, extra_words

def letter_checker(temp_list_word, inp_list, wrong_letter_dict_copy):
    #copy old letter_dict so it can update
    '''
    Checking if the inputted letters are the same as the requested ones
    '''
    i = wrong_am_letter = 0
    wrong_letter_dict = wrong_letter_dict_copy #outside the loop so it persists
    while i < len(temp_list_word):
        letter_list_temp = [] #inside loop so it resets
        letter_list_inp = []
        _ = 0
        for letter in temp_list_word[i]:
            letter_list_temp.append(letter)
        try:
            for letter in inp_list[i]:
                letter_list_inp.append(letter)
        except IndexError:
            pass
        for letter in letter_list_temp:
            try:
                if letter != letter_list_inp[_]:
                    if letter in wrong_letter_dict:
                        wrong_letter_dict[letter] += 1
                    else:
                        wrong_letter_dict[letter] = 1
                    wrong_am_letter += 1
            except IndexError:
                if letter in wrong_letter_dict:
                    wrong_letter_dict[letter] += 1
                else:
                    wrong_letter_dict[letter] = 1
                wrong_am_letter += 1
            _ += 1
        i += 1
    wrong_letter_dict = wrong_letter_dict_sorter(wrong_letter_dict)
    return wrong_am_letter, wrong_letter_dict #returns a tuple with the info. check printer

def wrong_letter_dict_sorter(wrong_letter_dict_copy):
    '''
    Sorting by amount and then by alphabet, case insensitive
    '''
    wrong_letter_list = sorted(wrong_letter_dict_copy.items(), key=sort_key, reverse=True)
    #sorted returns a list & .items() returns tuple. Change it back into dict.
    return dict(wrong_letter_list)

def wrong_letter_dict_printer(wrong_letter_dict):
    '''
    prints the items inside a dict-
    '''
    for key in wrong_letter_dict:
        print(f"{key} | {wrong_letter_dict[key]}")

def chrono_data(time_seconds_copy):
    '''
    Time handler, compacts the information into tuple to avoid too many args in function calls.
    '''
    time_seconds = time_seconds_copy
    minutes_display = 0
    seconds_display = time_seconds
    minutes_for_calc = time_seconds_copy // 60

    if time_seconds > 30:
        time_seconds = 0
        minutes_for_calc += 1
    if time_seconds < 30:
        time_seconds = 0
    if minutes_for_calc == 0:
        minutes_for_calc = 1

    time_seconds_rounded = (minutes_for_calc * 60) + time_seconds
    while seconds_display > 60:
        minutes_display += 1
        seconds_display -= 60
    #[0] = minutes_display, [1] = seconds_display, [2] = time_seconds_rounded
    return minutes_display, seconds_display, time_seconds_rounded

def statistics(time_seconds_copy, word_data, percentage_data, wrong_letter_dict, line=""):
    '''
    Handles all the statistics with time and accuracy, calls the respective functions.
    '''
    time_data = chrono_data(time_seconds_copy)
    gross_wpm = (word_data[2] / time_data[2]) * 60
    wrong_words_total = word_data[1] + word_data[0]
    net_wpm = gross_wpm - ((wrong_words_total / time_data[2]) * 60)
    wpm_data = [0, 0, 0]
    wpm_data[0] = gross_wpm
    wpm_data[1] = net_wpm
    try:
        accuracy = round(((net_wpm / gross_wpm) * 100), 1)
    except ZeroDivisionError:
        accuracy = 100
    wpm_data[2] = accuracy
    printer(percentage_data, wrong_letter_dict,
            time_data, wpm_data, line)
    return net_wpm

def printer(percentage_data, wrong_letter_dict,
            time_data, wpm_data, line):
    '''
    Prints all the statistics with time and accuracy
    '''
    print(chr(27) + "[2J" + chr(27) + "[;H") # ref marvin
    print(f"Word Precision: {percentage_data[0]}%")
    print(f"Letter Precision: {percentage_data[1]}%")
    print("Wrong letters: {")
    wrong_letter_dict_printer(wrong_letter_dict)
    print("}")
    print(f"time: {time_data[0]} min, {round(time_data[1], 1)} sec")
    print(f"Gross WPM: {wpm_data[0]}")
    print(f"Net WPM: {wpm_data[1]}")
    print(f"Accuracy: {wpm_data[2]}%")
    if line != "":
        print(line)

def wpm_category(net_wpm):
    '''
    Giving the user an animal based on their net_wpm. 
    '''
    speed_animal = ""
    if 0 <= net_wpm < 5:
        speed_animal = "Sloth"
    elif 5 < net_wpm < 15:
        speed_animal = "Snail"
    elif 15 < net_wpm < 30:
        speed_animal = "Manatee"
    elif 30 < net_wpm < 40:
        speed_animal = "Human"
    elif 40 < net_wpm < 50:
        speed_animal = "Gazelle"
    elif 50 < net_wpm < 60:
        speed_animal = "Ostrich"
    elif 60 < net_wpm < 70:
        speed_animal = "Cheetah"
    elif 70 < net_wpm < 80:
        speed_animal = "Swordfish"
    elif 80 < net_wpm < 90:
        speed_animal = "Spur-winged Goose"
    elif 90 < net_wpm < 100:
        speed_animal = "White-throated Needletail"
    elif 100 < net_wpm < 120:
        speed_animal = "Golden Eagle"
    else:
        speed_animal = "Peregrine Falcon"
    return speed_animal


def percentage_data_calculator(word_list, correct_am_words, correct_am_letters):
    '''
    Percentage calculator
    '''
    total_am_words = word_length_checker(word_list)
    total_am_letters = letter_length_checker(word_list)
    percentage_word = round((correct_am_words / total_am_words) * 100, 3)
    percentage_letter = round((correct_am_letters / total_am_letters) * 100, 2)
    return percentage_word, percentage_letter

def make_to_word_list(lines):
    '''
    Make lines into word list
    '''
    word_list = lines.split("\n")
    return word_list

def make_to_letter_list(lines):
    '''
    Makes lines into letter list
    '''
    letter_list = lines.split(" ")
    return letter_list

def random_speed_test():
    '''
    Random character for a set amount of time
    '''
    characters = ("a b c d e f g h i j k l m n o p q r s t " +
                "u v w x y z A B C D E F G H I J K L M N O P " + 
                "Q R S T U V W X Y Z 1 2 3 4 5 6 7 8 9 0 ! # " +
                "€ % & / ( ) = ? _ . : ; - ' * ^ < > § ° ´ `")
    letter_list = make_to_letter_list(characters)
    wrong_am = total_am = total_time = 0
    wrong_letter_dict = {}
    time_ask = int(input("How many seconds do you want to go?"))
    start_time = time.time()
    while total_time < time_ask:
        random_int = random.randint(0, len(letter_list))
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(f"{letter_list[random_int]}")
        user_inp = input("")
        if user_inp != letter_list[random_int]:
            if letter_list[random_int] in wrong_letter_dict:
                wrong_letter_dict[letter_list[random_int]] += 1
                wrong_am += 1
            else:
                wrong_letter_dict[letter_list[random_int]] = 1
                wrong_am += 1
        total_am += 1
        current_time = time.time()
        total_time = current_time - start_time
    input("Well done, practice is over. Press enter for results...")
    random_speed_test_printer(wrong_letter_dict, wrong_am, total_am, time_ask)

def random_speed_test_printer(wrong_letter_dict, wrong_am, total_am, time_ask):
    '''
    Printer functionality for random_speed_test.
    '''
    print("Wrong letters{")
    wrong_letter_dict_printer(wrong_letter_dict_sorter(wrong_letter_dict))
    print("}")
    print(f"wrong percent: {round((wrong_am / total_am) * 100, 2)}%")
    print(f"Letter Per Min: {(total_am / time_ask) * 60}")
    input("Enter to return to main menu...")

def main(difficulty):
    '''
    Main functionality of the program, calls all other 
    functions and handles percentages and persisting values.
    '''
    word_list = make_to_word_list(fh.readfile(difficulty))
    correct_am_words = word_length_checker(word_list)
    correct_am_letters = letter_length_checker(word_list)
    wrong_letter_dict = {}
    word_data = [0, 0, 0]
    start_time = time.time() #starts taking the time here, lets call value X
    end_time = start_time
    for line in word_list:
        percentage_data = percentage_data_calculator(word_list, correct_am_words,
                                                    correct_am_letters)
        statistics((end_time - start_time), word_data, percentage_data, wrong_letter_dict, line)
        inp = input("")
        end_time = time.time() #records the time over here, effective time is x - endtime
        #the splits are effectively the lists but instead of wasting space
        #i've added them as parameters instantly directly.
        word_data[2] += len(inp.split(" ")) #Written words
        data_from_word_func = word_checker(line.split(" "), inp.split(" ")) #returns tuple
        word_data[1] += data_from_word_func[1] # extra words
        correct_am_words -= data_from_word_func[0]
        word_data[0] += data_from_word_func[0] # wrong am of words
        data_from_letter_func = letter_checker(line.split(" "), inp.split(" "), wrong_letter_dict)
        print(data_from_letter_func)
        #data_from_func is used to get info from the function
        #and then splitting it up into its uses inside this one.
        correct_am_letters -= data_from_letter_func[0]     #removes the wrong amount
        wrong_letter_dict = data_from_letter_func[1]
    print(chr(27) + "[2J" + chr(27) + "[;H")
    input("Congrats, you have finished. Press enter for results...")
    percentage_data = percentage_data_calculator(word_list, correct_am_words, correct_am_letters)
    net_wpm = statistics((end_time - start_time), word_data, percentage_data, wrong_letter_dict)
    print(f"You write as fast as a {wpm_category(net_wpm)}")
    username = input("What is your name? --->  ")
    fh.writefile(username, percentage_data[0], difficulty)
