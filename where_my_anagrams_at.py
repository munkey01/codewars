'''
Challenge:
Take two arguments into a function. First argument is a word and the second is a list of words. Return all words that are an anagram of the first argument.

Reflection:
I tried something new with this challenge (see short_anagrams()). The long_anagrams() function was my first attempt at a solution. It sorts the original word and words[] and compares the resulting lists to see if they are equivalent. If so, then long_anagrams() appends the word to a list to return later.

The short_anagrams() function uses list comprehension to achieve the goal. I have never used list comprehension before, but it is definitely less intimidating now; maybe even insultingly easy.
The layout goes like this:
new_list = [<<item to add to new list>> for item in other_list if <<test condition>> is true for item] 
The goal of list comprehension (as far as I can tell) is to help build simple lists based on individual test conditions (things that would otherwise use a traditional for loop and if statements and maybe additional, temporary variables). 
'''

def short_anagrams(word, words): #uses list comprehension
    return [x for x in words if sorted(x) == sorted(word)]

def long_anagrams(word, words):
    anagrams = []
    orig_sorted = list(word)
    orig_sorted.sort()
    for w in words:
        w_sorted = list(w)
        w_sorted.sort()
        if w_sorted == orig_sorted:
            anagrams.append(w)
    return anagrams
