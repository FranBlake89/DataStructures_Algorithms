# copy over your code from lab 1 to this file

def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

def sum_to_goal(list, goalValue):
    multVal = 0
    if goalValue > 0:
        for element in list:
            numRest = goalValue - element
            for newEle in list:
                if(newEle == numRest):
                    multVal = element * newEle
    else:
        return multVal

    return multVal

    