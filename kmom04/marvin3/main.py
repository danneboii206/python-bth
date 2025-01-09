#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
A terminal script that can do different things for the user in one single script.
'''

import marvin1
import marvin2
import inventory

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

# The code is inside a while loop, everything is.
# Thus, all the code will be constantly run untill q is pressed
# The while loop only breaks after pressing q, or stopping
# the program manually.

bag = []

def main():
    '''
    The main functionality of the script that can answer different questions
    depending on the choice the user makes.
    '''
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
        print("9) SSN creator")
        print("10) Acronym maker")
        print("11) String scrambler")
        print("12) Index detector")
        print("New inventory commands! inv, inv pick, inv drop & inv swap")
        print("q) Quit.")
        print("try out my new inv commands!")

        choice = input("--> ")

        if choice == "q": 
            print("Bye, bye - cya in hell!")
            stop = True

    # ask for name, print out name
        elif choice == "1":
            marvin1.greet()

    # ask for celcius, print out fahrenheit
        elif choice == "2":
            marvin1.celsius_to_fahrenheit()

    # ask for points, print out grade
    # % to Grade(s);       >= 90% = A
    #                      >= 80% = B
    #                      >= 70% = C
    #                      >= 60% = D
    #                      <  60% = F
        elif choice == "3":
            marvin1.points_to_grade()

    # ask for numbers, print out sum & average
        elif choice == "4":
            marvin1.sum_and_average()

    # ask for input, seperate char by - and
    # add +1 of the same char per seperation
        elif choice == "5":
            marvin1.hyphen_string()

    #ask for number, save that number and print if
    #new number is bigger or smaller than old number.
        elif choice == "6":
            marvin1.compare_numbers()

    #Checking validation of social sec. numbers
        elif choice == "7":
            marvin1.validate_ssn()

    #Input from user, convert to robber language
        elif choice == "8":
            marvin1.robber_language()

    #Creates a ssn with the help of birthdate
        elif choice == "9":
            inp = input("Enter birthdate to create SSN \n >>> ")
            print(marvin2.create_ssn(inp))

    #Gets acronyms
        elif choice == "10":
            inp = input("Enter text to randomize order >>> \n >>> ")
            print(marvin2.get_acronym(inp))

        elif choice == "11":
            inp = input("Enter a text to scramble \n >>> ")
            print(f"{inp} --> {marvin2.randomize_string(inp)}")

        elif choice == "12":
            inp1 = input("Enter your desired string")
            inp2 = input("enter your desired variable")
            print(marvin2.find_all_indexes(inp1,inp2))

        elif "inv pick" in choice:
            resstring = choice.replace("inv pick ", "")
            reslist = resstring.split(" ")
            in1 = reslist[0]
            if len(reslist) > 1:
                in2 = reslist[1]
                inventory.pick(bag, in1, in2)
            else:
                inventory.pick(bag, in1)
            
        elif choice == "inv":
            inventory.inventory(bag)
            
        elif "inv drop" in choice:
            resstring = choice.replace("inv drop ", "")
            inventory.drop(bag, resstring)

        elif "inv swap" in choice:
            resstring = choice.replace("inv swap ", "")
            reslist = resstring.split(" ")
            item1 = reslist[0]
            item2 = reslist[1]
            inventory.swap(bag, item1, item2)

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        if not stop:
            input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
