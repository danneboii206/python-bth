'''
Text analyzer
'''

import analyzer

def main():
    '''
    Start the program
    '''
    fname = "phil.txt"

    stop = False
    while not stop:
        print("lines) Line count")
        print("words) Word count")
        print("letters) Letter count")
        print("word_frequency) 7 most used words")
        print("letter_frequency) 7 most used letters")
        print("all) Do all the named functions")
        print("change) Change file for analysis")
        print("q) Quit the program")

        choice = input("--> ")
        if choice == "q":
            print("Exiting")
            stop = True
        elif choice == "lines":
            line_am = analyzer.check_lines(fname)
            print(line_am)
        elif choice == "words":
            word_am = analyzer.check_words(fname)
            print(word_am)
        elif choice == "letters":
            letter_am = analyzer.check_letters(fname)
            print(letter_am)
        elif choice == "word_frequency":
            word_freq = analyzer.word_frequency(fname)
            print(word_freq)
        elif choice == "letter_frequency":
            letter_freq = analyzer.letter_frequency(fname)
            print(letter_freq)
        elif choice == "all":
            line_am = analyzer.check_lines(fname)
            word_am = analyzer.check_words(fname)
            letter_am = analyzer.check_letters(fname)
            word_freq= analyzer.word_frequency(fname)
            letter_freq = analyzer.letter_frequency(fname)
            print(f"{line_am}\n{word_am}\n{letter_am}\n{word_freq}\n{letter_freq}")
        elif choice == "change":
            inp = input("What file? >>> ")
            fname = inp
if __name__ == "__main__":
    main()
