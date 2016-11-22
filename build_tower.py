'''
Challenge:
Print a tower with a given number of floors. The tower should be a list in the format of:
[ ['  *  '],
  [' *** '],
  ['*****'] ]
  
Reflection:
This is the first time that I have used map and the first time I have used lambda. Map allows you to run a function over a set of iterables and lambda allows you to establish an "in-line" function. Combined, this allowed me to create the tower with 1 line of code. One other solution that I like/envy is in the form of list comprehension:
    return [" " * (n - i - 1) + "*" * (2*i + 1) + " " * (n - i - 1) for i in range(n)]
I tried to use list comprehension but apparently approached it in a backward fashion. I need to call the string constructor for each item in the range prior to the "in-line" for loop.
'''

def tower_builder(n):
    return list(map(lambda i: (' ' * (n-i-1) + '*' * (2*i+1) + ' '*(n-i-1)), range(n)))
