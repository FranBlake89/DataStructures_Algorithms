# Analysis and Reflection for Lab 1
## function 1:

Analyze the following function with respect to number

```python
def function1(value, number):
	if (number == 0):
		return 1
	elif (number == 1):
		return value
	else:
		return value * function1(value, number-1)
```

	T(n) = O(1) + T(n-1)
	T(n-1) = O(1) + T(n-2)
	T(n) = O(1) * n
	In conclusion the time complexity is:  
	T(n) = O(n)


---
## function 2:

Analyze function2 with respect to the length of the mystring.  Hint, you will need to set up two mathematical functions for operator counting.  one for function2 and the other for recursive_function2

```python

def recursive_function2(mystring,a, b):
	if(a >= b ):
		return True
	else:
		if(mystring[a] != mystring[b]):
			return False
		else:
			return recursive_function2(mystring,a+1,b-1)

def function2(mystring):
	return recursive_function2(mystring, 0,len(mystring)-1)

```
	T(n) = T(n-2) + O(1)
	T(n-2) = T(n-4) + O(1)
	T(n) = O(1) + .....
	T(n) = O(1) * (n/2)
	The time complexity oif the function is:
	T(n) = O(n)
---

### function 3 (optional challenge):

Analyze the following function with respect to number


```python
def function3(value, number):
	if (number == 0):
		return 1				#1 -> O(1)
	elif (number == 1):				#1
		return value				#1 -> O(n)
	else:
		half = number // 2			#2
		result = function3(value, half)		# log(number)
		if (number % 2 == 0):			#2
			return result * result		#1
		else:
			return value * result * result	#2

```
	For number == 0 or number == 1, the time complexity is O(1).
	For larger values of number, the time complexity is O(log(number)).
---
## Part C reflection

Answer the following questions

1. Describe how to a approach writing recursive functions, what steps do you take?
	The first step to approach to recursive function, it is idetify the base case or stop condition for the recursion, avoiding the infinite loop. Then, we need to define the recursive case by breaking down the problem into smaller problems, calling the function recursively when applicable. Finally, analize and dolve a recurrrence relation to determine the time complexity of the function.

2. Describe the process of analyzing recursive functions.  How does it differ from from analyzing non-recursive functions?  How is it the same? 
	On basics is the same, using similar techniques and identification of base cases. Analize recursive functions involves evaluate the time complexity and code size. On the other hanh, a Non-recursive function has simpler code and lower time complexity.It is important to note the analysis in recursive functions require undestand recursion pattern and the number of recursive calls made, which is not applicable in non-recursive function. 
