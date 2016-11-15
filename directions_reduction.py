'''
Challenge:
Take a list of directions (north, south, east, west) and simplify the travel plan by removing opposites next to each other.
This removal process should be repeated as many times as necessary.

Reflection:
I had some problems with this challenge, most of which were related to index being out of range.
I installed break statements if certains conditions were met. This helped me clear most tests, but not all.
Finally decided on using a try and except statement. Try to test the conditions in the if-statement (line 29), if it fails then bail out of loop.
Also, I used recursion for the first time during this challenge. It seems to work well since it forces the list of directions to be rechecked, from the beginning, everytime adjustments are made.
Lastly, line 30 and and 31 gave me trouble. I had them switched. Problem: pop(i) changes the length and causes i+1 to move to i.
'''

def isOpposite(a,b):
    if (a == "NORTH" and b == "SOUTH") or (b == "NORTH" and a == "SOUTH"):
        return True
    elif (a == "EAST" and b == "WEST") or (b == "EAST" and a == "WEST"):
        return True
    else:
        return False

def dirReduc(arr):
    #use recursion to continue simplifcation until unable to do so
    #maybe recursion isn't needed with the continue statement...instead of looping through the rest
    #then starting over, we can just start over each time.
    for i in range(len(arr)-1):
        try:
            if isOpposite(arr[i],arr[i+1]):
                arr.pop(i+1)
                arr.pop(i)
                dirReduc(arr) #or recursion? call dirReduc(arr)? continue?
        except:
            break
    return arr
