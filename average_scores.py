'''
Challenge:
Find the mean of all numbers in an array without the use of loops.

Reflection:
Make sure to pay attention to rounding differences between Python 2 and Python 3.
Python 2 rounds to the nearest whole number, 0.5 rounded upwards. However, this method tends to favor large numbers.
Python 3 rounds to the nearest even number, typically resulting in higher overall accuracy.
Because of this, I used the round() function in order to keep Python 2 methodology.
'''

def average(array): 
  return round((sum(array))/len(array))
