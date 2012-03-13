# really terse palindrome checker 

from sys import argv

def check_phrase(phrase):
    phrase = phrase.lower()
    phrase = phrase.replace(' ','')
    return phrase == phrase[::-1]

if __name__ == "__main__": 
    print check_phrase(str(argv[1]))
