# Write the code for your lab 1 here.  Read the specs carefully.
# Function name must be exactly as provided.
# Names of variables and parameters can be whatever you wish it to be
#
# To test, run the following command :
#     python test_lab1.py
#
# Author: Francisco Castillo
# Student Number: 148904212
#
def lower(str):
    new_str = ""

    for c in str:
        if "A" <= c <= "Z":
            new_str += chr(ord(c) - ord('A') + ord('a'))
        else:
            new_str += c

    return new_str


def wins_rock_scissors_paper(param_1, param_2):
    value_p1 = lower(param_1)
    value_p2 = lower(param_2)

    if value_p1 == 'rock' and value_p2 == 'scissors':
        return True
    elif value_p1 == 'paper' and value_p2 == 'rock':
        return True
    elif value_p1 == 'scissors' and value_p2 == 'paper':
        return True
    else:
        return False


def factorial(num):
    temp = num
    result = 1

    while temp > 0:
        if result == 1:
            result = temp
        else:
            result = result * (temp)
        temp = temp - 1

    return result


def fibonacci(num):
    val = 0
    if num == 0:
        return val
    elif num == 1 or num == 2:
        val = 1
        return val
    else:
        return fibonacci(num-1) + fibonacci(num-2)


def sum_to_goal(list, goalValue):
    multVal = 0
    if goalValue > 0:
        for element in list:
            numRest = goalValue - element
            for newEle in list:
                if (newEle == numRest):
                    multVal = element * newEle
    else:
        return multVal

    return multVal


class UpCounter:
    def __init__(self, num):
        self.numbertracked = num
        self.counter = 0

    def count(self):
        if self.counter == 0:
            self.counter = 1

        return self.counter

    def update(self):
        if self.counter == 1:
            self.counter = self.numbertracked
        else:
            self.counter = self.counter + self.numbertracked


class DownCounter(UpCounter):
    def update(self):
        if self.counter == 0:
            self.counter = self.numbertracked * (-1)
        else:
            self.counter = self.counter + (self.numbertracked * (-1))
