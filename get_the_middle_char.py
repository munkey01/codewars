'''
Challenge:
Return the middle char (or middle two if even length string).

Reflection:
This was a Kata that I started when I first found Codewars and apparently didn't finish.
I first chose to test for odd(ness) using modulo 3 and decided to change to even(ness).
I had to edit the end portion of my string slicing due to the fact that the ending index is not included in the returned string (added +1 to fix). 
'''

def get_middle(s):
    if len(s) % 2 == 0:
        return s[len(s)/2-1:len(s)/2+1]
    else:
        return s[len(s)/2]
        
