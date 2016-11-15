'''
Challenge:
Return True if the string contains only alphanumeric characters. Return False otherwise.

Reflection:
Apparently Python has a function for this -- isalnum() . I could have used this instead of combining isnumeric() and isalpha() and iterating over the string after converting it into a set.
'''

def alphanumeric(string):
    for i in set(string):
        if i.isnumeric() or i.isalpha():
          continue
        else:
            return False
    return True
