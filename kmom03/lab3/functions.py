'''
Different functions inside answer.py
'''


def multiplication(int1,int2):
    '''
    Multiplies two values
    '''
    res = int1 * int2
    return res

def funny_word(text):
    '''
    Prepends "is a funny word" to string
    '''
    res = (f"{text} is a funny word")
    return res

def decider(text):
    '''
    Sorts out two different alternatives
    '''
    if text.isdigit() is True:
        inttext = int(text)
        res = multiplication(inttext,inttext)
    else:
        res = funny_word(text)
    return res

def doubledecider(text, num):
    '''
    Splits up two different types (int and str)
    '''
    word = funny_word(text)
    result = multiplication(num,num)
    res = (f"{word} and the square is {result}")
    return res
