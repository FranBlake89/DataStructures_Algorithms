# Lab 1

## Due: Feb 17, 2024

## Objectives:

* Learn the basics of Python programming



## Part A Coding: 

This part of the lab will introduce you to the basics of python programming.  **You are not allowed to use any library functions for this lab unless it is specifically stated in the specification**

Write the following functions in lab1.py

The function names must be exactly as specified.  The number and order of arguments must be the same.  

### Function 1: 

Name: wins_rock_scissors_paper

Parameters: 2 strings

Return: a boolean value

Description: this function is passed two strings.  Each of the two strings are going to be  one of 3 values:
* rock
* paper
* scissors


The strings may have any casing. Rock, ROCK, roCK are all possible and valid. 

The first string represents what the player threw in a game of rocks paper scissors.  The second string represents what the opponent threw.  This function returns true, if the player won, false if it was a tie or a lose.

In a game of rock, paper, scissors, each player chooses "throws" one of the 3 items. Winner is determined by the following rules
- rock beats scissors
- paper beats rock
- scissors beats paper

### Function 2:

Name:  factorial

Parameters: a number (int)

Return: a number (int)

Description: this function is passed a non-negative integer, that we will call n in this description.  function returns n! (pronounced n fatorial).  n! = n * (n-1) * (n-2)... *  1  Thus, 3! = 3 * 2 * 1.  Note that 0! is 1 by definition.

### Function 3:

Name: fibonacci

Parameters: a number (int)

Return: a number (int)

Description: this function is passed a non-negative integer, that we will call n in this description.  function returns the nth fibonacci number in the fibonacci sequence.  

let $F_n$ represent the nth fibonacci number.

* $F_0 = 0$
* $F_1 = 1$
* $F_2 = 1$
* $F_3 = 2$
* $F_4 = 3$
...
* $F_n = F_{n-1} + F_{n-2}$

the nth fibonacci number is the sum of the 2 previous fibonacci numbers.

### Function 4:

Name: sum_to_goal

Parameters: list of numbers, and a goal (number) 

Return: a number

Description: This function finds the two numbers in the list that sum up to the goal value. Function returns the product of the two numbers(the product is the result of multiplying the two numbers together) .  If there are no two numbers that when summed results in the goal state, function returns 0

### Python Objects

In lab1.py

Create a python class called **UpCounter**.

A **UpCounter** keeps track of a number.  the number can be increased by a fixed step size

When a counter is initialized, it is given a a step size. If no step size is given, the step size is assumed to be 1. The counter always starts at a count value of 0

The counter class has three functions:

* count() - returns the current counter value
* update() - increases the counter value by stepsize

Derive a python class call **DownCounter** which is inherited from **UpCounter**

A **DownCounter** is initialized with same arguments as an **UpCounter**.  The only difference is that when the update() function is called, the counter decrements the counter value by stepsize






