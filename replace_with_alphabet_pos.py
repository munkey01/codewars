'''
Challenge:
Replace each letter in a string with its corresponding position in the alphabet.
Separate each translated character with a space, ignore non-alphabetic characters.

Reflection:
Next time I can avoid the task of creating a list of the alphabet and instead just make a string ("abcde...").
Also, apparently ord(char) will return the chats unicode code point as an integer. So ord(c) - 96 will give the alphabetic position of a char.
I should learn more about list comprehension methodology (in line for loops).Separate each translated character with a space, ignore non-alphabetic characters:. 
'''

def alphabet_position(text):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    text = text.lower()
    result = ""
    for i in text:
        if i not in alphabet: 
            continue
        else:
            result += str(alphabet.index(i)+1) + ' '
    result = result[:-1] #trim trailing space
    return result
