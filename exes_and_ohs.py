'''
Challenge: 
Return True if number of x's and o's are equal in a string. Otherwise, return False. Should not be case sensitive.

Reflection:
By putting 'and' instead of '==' I would get True if x's and o's were both present, no matter the number of them.
This must be due to a return of any number by count being treated as a True value, therefore True and True returns True for xo().
By putting '==' in instead of 'and' I force the function to determine if the two values are equal to one another.
'''

def xo(s):
    return list(s.lower()).count('x') == list(s.lower()).count('o')
