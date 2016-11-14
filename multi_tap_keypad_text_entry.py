'''
Challenge:
Count the number of button presses are required to text a phrase using an old cellphone (without T9).

Reflection:
Unfortunately, the challenge description is incomplete. The challenge does not explain how the coder should handle non-alpha characters (such as ',.></?, etc). Code passed all tests except nonalpha test (I commented out  the lines that I attempted  to use to fix this). 
I first attempted to use a dictionary to lookup values then find the index of each value in the dictionary (key:['v','a','l','u','e','s']); however, this didn't work, maybe due to my own lack of practice with dictionaries.

'''

def presses(phrase):
    #create 2D array representing buttons with letters included
    buttons = [ [' ','0'], ['1'],['A','B','C','2'],['D','E','F','3'],
                ['G','H','I','4'],['J','K','L','5'],['M','N','O','6'],
                ['P','Q','R','S','7'],['T','U','V','8'],['W','X','Y','Z'] ]  
    total = 0
    
    #set all letters of the phrase to capital letters
    phrase = phrase.upper()
    
    #parse the phrase by character, determine which position in the array is the character (+1)
    for i in range(len(phrase)):
        for j in range(10):
            if phrase[i] in buttons[j]:
                total += buttons[j].index(phrase[i])+1
            #elif not phrase[i].isalpha() and not phrase[i].isnumeric() and phrase[i] != ' ':
            #    total += 1
    return total
