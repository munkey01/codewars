'''
Challenge:
Given two integers, find the sum of all numbers between them (including numbers themselves).

Reflection:
The for loop runs from the smallest of the two numbers to  the largest; this is due to the fact that a and b are not necessarily ordered. The +1 in conjucntion with the max() call forces the loop to be inclusive in its addition.
'''

def get_sum(a,b):
    total = 0
    for i in range(min(a,b),max(a,b)+1):
        total += i
    return total
