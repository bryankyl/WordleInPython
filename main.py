from colorama import init
from colorama import Fore, Back, Style

answer = "HELLO"

def isExactPlace(char, word, index) -> bool:
    if (char == word[index]):
        return True
    else:
        return False

def isIncluded(char, word) -> bool:
    flag = False
    for index in range(len(word)-1):
        if (char == word[index]):
            flag = True
    return flag

def showColour(a,b) -> str:
    if isExactPlace():
        colour = Fore.GREEN
    elif isIncluded():
        colour = Fore.YELLOW
    else:
        colour = Fore.RESET
    return colour

print(isExactPlace("A","APPLE", 0))
print(isIncluded("E","EAGLE"))


"""
def check(guess, answer):
    answer = answer.upper()
    return_string = ""
    for i in range(0,len(answer)):
        if guess[i] == answer[i]:
            return_string += (Fore.GREEN + guess[i])
        else:
            return_string += (Fore.RESET + guess[i])
    return return_string

print("Wordle Game in Python")
print("*"*21)

print(check("APPLE","apple"))

"""
"""
MAX_TIMES = 6
def guess(times) -> str:
    return input("Guess " + str(times) + " : ")

for times in range(MAX_TIMES):
    word = guess(times+1)
    for c in word:
        print(c.upper() , end="")
    print()
"""