'''
Challenge:
Count number of integers needed to complete series from smallest digit to largest.
Ex: [2,5,1] -> 2 since 3 and 4 are needed to complete series as 1,2,3,4,5

Reflection:
Finished easily. Main thing: had an issue when test gave empty list (exception thrown by min()).
I combated this using try and except calls. I wonder if there is a better way?
'''

def consecutive(arr):
    total = 0
    try:
        for i in range(min(arr)+1,max(arr)):
            if i not in arr:
                total += 1
    except:
        return total
    return total
