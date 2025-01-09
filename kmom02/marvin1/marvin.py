#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Lucy with a simple menu to start up with.
Lucy doesnt do anything, just presents a menu with some choices.
You should add functinoality to Lucy.
"""

lucy_image = r'''
   , ,, ,                              
   | || |    ,/  _____  \.             
   \_||_/    ||_/     \_||             
     ||       \_| . . |_/              
     ||         |  L  |                
    ,||         |`==='|                
    |>|      ___`>  -<'___             
    |>|\    /             \            
    \>| \  /  ,    .    .  |           
     ||  \/  /| .  |  . |  |           
     ||\  ` / | ___|___ |  |     (     
  (( || `--'  | _______ |  |     ))  ( 
(  )\|| (  )\ | - --- - | -| (  ( \  ))
(\/  || ))/ ( | -- - -- |  | )) )  \(( 
 ( ()||((( ())|         |  |( (( () ) (credit to hjm)
    '''


'''
Its an eternal loop, until q is pressed.
It should check the choice done by the user and call a appropriate
function.
'''

# The code is inside a while loop, everything is.
# Thus, all the code will be constantly run untill q is pressed
# The while loop only breaks after pressing q, or stopping
# the program manually.

stop = False
while not stop:
    print(chr(27) + "[2J" + chr(27) + "[;H") # creates spaces
    print(lucy_image) 
    print("Hi, I'm Lucy. I know and see all. What is your command?")
    print("1) Present yourself to Lucy.")
    print("2) Convert from celcius to fahrenheit.")
    print("3) Calculate your grade")
    print("4) Sum and average of inputed numbers")
    print("5) String seperation with addition of letters per seperation")
    print("6) Lower or bigger numbers game")
    print("7) SSN Validation")
    print("8) Robber language converter")
    print("q) Quit.")

    choice = input("--> ")

    if choice == "q": 
        print("Bye, bye - cya in hell!")
        stop = True

# ask for name, print out name
    elif choice == "1":
        name = input("What is your name? ")
        print("Lucy says:\n")
        print(f"Hello {name} - wassaaaap?")
        print("What do you desire?")

# ask for celcius, print out fahrenheit
    elif choice == "2":
        print("Lucy says:\n")
        celcius = float(input("Write the degrees in fahrenheit "))
        # Fahrenheit formula ((C° x 9/5) + 32)
        fahrenheit = round((celcius * 9/5 + 32), 2)
        print(f"The requested temperature is {fahrenheit} °F")
        print("A whole lot colder than hell...")

# ask for points, print out grade
# % to Grade(s);       >= 90% = A
#                      >= 80% = B
#                      >= 70% = C
#                      >= 60% = D
#                      <  60% = F
    elif choice == "3":
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

# ask for numbers, print out sum & average
    elif choice == "4":
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

# ask for input, seperate char by - and
# add +1 of the same char per seperation
    elif choice == "5":
        text = input("Write anything u want\n")
        len_text = len(text)
        result_text = ""
        i = 0
        #do the heavy work by looping
        while i != len_text:
            result_text += text[0 + i] * (i + 1)
            i = i + 1
            if i != (len_text):
                result_text += "-"
        #
        print(result_text)

#ask for number, save that number and print if
#new number is bigger or smaller than old number.
    elif choice == "6":
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
            #only for the first number
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

#Checking validation of social sec. numbers
    elif choice == "7":
        total = 0
        i = 2
        int_num = 0
        #input of ssn
        ssn = input("Please write your social security number: ")
        #looping through the numbers
        for number in ssn:
            if number == "-":
                continue
            if i % 2 == 0:
                ind_num = (int(number) * 2)
                if ind_num > 9:
                    for num in str(ind_num):
                        total += int(num)
                else:
                    total += (int(number) * 2)
            else:
                total += int(number)
            i += 1
        #testing validation
        if total % 10 == 0 and i == 12:
            print("Valid")
        else:
            print("Not valid")

#Input from user, convert to robber language
    elif choice == "8":
        consonants = "aeiouyåäö"
        ans = ""
        inp = input("Write a message to convert to robber language: ")
        #looping through the letters
        for char in inp.lower():
            if char in consonants:
                ans += str(char)
            else:
                ans += str(char) + "o" + str(char)
        #printing the results
        print(ans)

    else:
        print("That is not a valid choice. You can only choose from the menu.")

    if not stop:
        input("\nPress enter to continue...")
