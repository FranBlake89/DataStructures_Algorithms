# Lab 2


### function 1:

Analyze the following function with respect to number

```python
def function1(number):
	total=0;                       # 1

	for i in range(0,number):      # n + 1
		x = (i+1)                  # 2(n)
		total+=(x*x)               # 3(n) [total = total + (x*x)]

	return total                   # 1
```
$T(n) = 1 + n + 1 + 2n + 3n + 1$
$T(n) = n$
$T(n)= O(n)$

### function 2:

Analyze the following function with respect to number

```python
def function2(number):
	return  ((number)*(number+1)*(2*number + 1))//6 # 6  O(1), because is a constant 

```

$T(n) = O(1)$


### function 3:

Analyze the following with respect to the length of the list.  Note that the function call len() which returns the length of the list is constant (O(1)) with respect to the length of the list.
```python

def function3(list): 
	for i in range (0,len(list)-1):          # (n-1) + 2 
		for j in range(0,len(list)-1-i):     # (n-1)(n-1) + 3
			if(list[j]>list[j+1]):           # 2 [(n-1) (n-1)]
				tmp=list[j]                  # 1 [(n-1)(n-1)]
				list[j]=list[j+1]            # 2 [(n-1)(n-1)]
				list[j+1]=tmp                # 2 [(n-1)(n-1)]

```

$T(n) = O(n^(2))$


### function 4:

Analyze the following function with respect to number

```python
def function4(number):
	total=1                         # 1
	for i in range(1 to number):    # (n - 1) + 1
		total=total*(i+1)           # 3 (n)
	return total                    # 1
```
Formula to get number of operations in for loop with range: $$n - i + 1$$

T(n) = O(n)

## In class portion


### Group members
List the members of your group member below:

	* Name 
	* Marife Dela Torre
	* Francisco Castillo
	* John Aeron Aragones 
	* Naman

### Timing Data
Note, if a groupmate did not complete lab1, simply put 0.0 in for the times, it is ok if there is something missing.

| Team member | Timing for fibonacci | Timing for sum_to_number | 
|---|---|---|
| Francisco Castillo |  2.543 | 0.679 |
| John Aeron Aragones | 9.700 | 0.827 |
| Marife Dela Torre | 7.501 | 0.306 |
| Naman | 5.799 | 0.019 |


### Summary 

| function | fastest | slowest | difference
|---|---|---|---|
|sum_to_number | 0.019 | 0.827 | 0.808 |
|fibonacci | 2.543 | 9.700 | 7.157 |


### Discussion:

Look at the code from lab 1 and discuss the differences between fastest/slowest versions. Was it a difference in syntax? A difference in approach?  Write down your observations.

For the function "sum_to_number" the major difference is in the aproach and syntax, because the fastest code uses logarithmic search instead of "normal" for-loops with conditionals, having a time complexity of $O log n$. 
On the other hand, in the function for fibonacci the fastest code uses recursion to find the total number, while the slower one prefers to use a lot of conditionals and a for-loop to achive the same goal, which has an impact on the time complexity. 
    

## Reflection

1. Considering the solutions you saw when looking at the lab 1 code, what differences did you see between fastest and slowest versions of code?
2. Was there a difference in terms of usage of space resource?  Did one algorithm use more/less space (memory)?  
3. What sort of conclusions can you draw based on your observations?

As I have written before, the use of recursion and logarithmic search have a real impact on time complexity and memory usage compared to just using for-loops and conditional, with the latter having this last the highest time complexity and memory usage impacting code performance. 

In conclusion, we can notice how useful recursion and logarithmic search are when we have a large amount of data. This is key when we work on real-world projects, where resources may be limited and we need to handle a large amount of data.

