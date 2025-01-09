'''
Keyboard writing speed test
'''

import checker as ch
import filehandler as fh

def main():
    '''
    Main program starter, handles alternatives.
    '''
    stop = False
    while not stop:
        print(chr(27) + "[2J" + chr(27) + "[;H") # creates spaces, ref marvin
        print("1) Speed test on easy")
        print("2) Speed test on medium")
        print("3) Speed test on hard")
        print("4) Score list")
        print("5) Train with random characters")
        print("q) Quit the program")
        # main loop
        choice = input("---> ")
        if choice == "q":
            print("Thanks for playing!")
            stop = True
        elif choice == "1":
            difficulty = "easy.txt"
            ch.main(difficulty)
        elif choice == "2":
            difficulty = "medium.txt"
            ch.main(difficulty)
        elif choice == "3":
            difficulty = "hard.txt"
            ch.main(difficulty)
        elif choice == "4":
            fh.print_score()
        elif choice == "5":
            ch.random_speed_test()

if __name__ == "__main__":
    main()
