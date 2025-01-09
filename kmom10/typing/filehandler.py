'''
File handler for the speed test
'''

def readfile(difficulty):
    '''
    Reads the file, returns list of lines
    '''
    with open(difficulty, "r", encoding="UTF-8") as fhand:
        lines = fhand.read()
    return lines

def writefile(username, word_precision, difficulty):
    '''
    Writes high-score
    '''
    diff = difficulty.split(".txt")
    with open("score.txt", "+a", encoding="UTF-8") as fhand:
        fhand.write(f"{username} | {word_precision} | {diff[0]} \n")


def print_score():
    '''
    Prints score.txt
    '''
    lines = readfile("score.txt")
    print(lines)
    input("Press enter to continue...")
