# Assignment 2

## Repo Creation Due Date: Wednesday, July 4

## Assignment Due Date: Monday, July 23

### This assignment is worth 12% of your final grade.

### Late penalties

* up to 1 week late - 10%
* 10% per day there after to a maximum of 50%

### Repo/Group Penalties:

10% deduction will be applied to **each** (ie more than one penalty can apply) of the following ...so follow the instructions carefully!  If there are technical issues, you can reach out to your professors and they will help you solve them. (note.. not following instructions are not technical errors).

* Repo creation is due on July 4. Any repos created after July 4 will receive a 10% deduction for the team.  Repos must be created AND all members must be joined into repo by this date.
* Creating more than 1 repo for your team.  Remember.. 1 person creates the team, everyone else joins.  Creating more than one repo for your team will result in a 10% deduction
* Any repos that fail to follow naming instructions on repo creation and thus requiring a manual fix will receive 10% deduction
* Any need to shift people due to improper joining may also receive a 10% deduction.
* Any one creating repos to work on their own will receive a 10% deduction.  

## Group Creation

In this assignment you can choose to work in a group of two or three.  You have until July 4 to create a team of your choosing.  After this date, students not in a team will be teamed up together by their profs.  **Working alone is not an option.**  In general we will try not to make adjustments to teams that you put together but there may be situations where we have no other ways of placing every student into a team without making changes to existing teams.  Our preference will always be to add someone to a team rather than breaking a team up and thus a three person team is very unlikely to be altered where as a two person team may end up with an additional person (but we will try to avoid this).  

**Make sure you are clear how many people you are working with and who they are before using the appropriate link.  You will not be able to modify this once you have created the teams.  When you create your team, your team name will need to use every member's seneca user name**

* [Repo Creation for teams of 2](repo-creation-g2.md)
* [Repo Creation for teams of 3](repo-creation-g3.md)

Your team will last for only 1 assignment.  If you decide that you were not able to work together after assignment 1, you can find new partners for the other assignments.  

## Work Divsion

* Every member of the team must contribute to the coding portions (parts C, and D) of the assignment.  Part C involves programming 2 classes, and part D has only one class.  As there are 3 coding components, we expect each member to be the lead author in one of the 3 sections.  It doesn't mean that other team members can't help ... but the lead should be the main contributer to that part of the assignment.
* Every member is expected to push their own code.
  * **it is NOT ok to use email or have just one person commit all the code. git/github is a professional tool that employers expect our graduates to know how to use, so learn it now.  If you aren't sure, check out the git tutorial listed in the resources section in course repo.**
* If we find that a member of the team did not author any code (according to commit records), that team member may be removed from the team and be required to redo the assignment with a grade deduction and late penalties.


## Assignment Completion

In order to for this assignment to be considered completed you must submit:

* a completed analysis of functions listed for (part A) - this part does NOT count as a programming component.  This cannot be the only contribution to the assignment by a team member.
* a successful run for part C, and D (green check for part C and part D in actions) - part C has two classes, and part D has one class...this offers one way for the work to be divided between the three members of the team.

Note: Assignment completion is the minimum requirements for your assignment.  It does not mean you will receive full marks.


## Assignment Objectives:

In this assignment, you will:

* Complete an analysis of multiple related functions for a class
* Implement hash tables
* Implement a graph

NOTE: **as this assignment is about implementing data structures, you are not allowed to make use of any python libraries or use built-in python data structures and functions unless specified.  If you are not sure, please ask your professor.  Any use a built-in libraries or functions without approval will result in having to redo the assignment with a grade penalty of -50%**

## Repository Setup

**This is Due by July 4**

In this assignment you can choose to work in a group of two or three partners.  If you are having trouble forming a group speak with your professor.  Decide what you want to do then use the instructions below to create your repo.  Follow the instructions carefully.

**Make sure you are clear how many people you are working with and who they are before using the appropriate link.  You will not be able to modify this once you have created the teams.**

* [Repo Creation for teams of 2](repo-creation-g2.md)
* [Repo Creation for teams of 3](repo-creation-g3.md)

Your team will last for only 1 assignment.  If you decide that you were not able to work together after this assignment, you can find new partners for the other assignments.  Every member of the team must contribute to the coding portions (parts C and D) of the assignment.  Every member is expected to push their own code.  If we find that a member of the team did not author any code (according to commit records), that team member may be required to redo the assignment with a grade deduction and late penalties.

## Overview


In this assignment you will look at several implementations of a Table.  There are three tasks:

1. Analyze the member functions of the class SortedTable (code for this is provided below).  This table is created using a sorted list.  It is not necessarily implemented well.  You will analyze the listed functions.
2. Offer suggestions on how to make the SortedTable more efficient.  After analyzing the functions, look at how it is done and come up with some changes that will make the code more efficient.
3. Implement a Hash table using linear probing for collision resolution, in two different ways.

## Table functions overview

We will explore 3 ways to implement a Table.  Each method will have a different internal structure but the functionality will be the same.  A table stores a set of key-value pairs which are also referred to as ***records***

The following specification describes an overview of the general functionalities of the table but it does not specify any specifics in terms of implementation.  In otherwords, it describes what it can do but doesn't specify any internal data strctures

---

```python
	def __init__(self, capacity=32):
```
The initializer for the table defaults the initial table capacity to 32.  It creates a list with capacity elements all initialized to None.

---

```python
	def insert(self, key, value):
```
This function adds a new key-value pair into the table. If a record with matching key already exists in the table, the function does not add the new key-value pair and returns False. Otherwise, function adds the new key-value pair into the table and returns True.  If adding a record will cause the table to be "too small" (defined in each class), the function will grow to acommodate the new record.

---

```python
	def modify(self, key, value):
```

This function modifies an existing key-value pair into the table. If no record with matching key exists in the table, the function does nothing and returns False. Otherwise, function modifies the existing value into the one passed into the function and returns True.

---


```python
	def remove(self, key):
```

This function removes the key-value pair with the matching key.  If no record with matching key exists in the table, the function does nothing and returns False.  Otherwise, record with matching key is removed and returns True

---

```python
	def search(self, key):
```

This function returns the value of the record with the matching key.  If no record with matching key exists in the table, function returns None

---

```python
	def capacity(self):
```

This function returns the number of spots in the table (available and used)

---

```python
	def __len__(self):
```
This function returns the number of Records stored in the table.

---


## Part A: Analyze the listed member functions of the SortedTable (12 marks)


Complete this part of the assignment in the a2.md file under the appropriate headings

Analyze the following functions with respect to the number of Records stored in the SortedTable

```python
	def insert(self, key, value):
	def modify(self, key, value):
	def remove(self, key):
	def search(self, key):
	def capacity(self):
	def __len__(self):

```


**Note: the code below is not necessarily the best way to write a table using a sorted array.  Outside of syntactic constructs, do not actually use this code for anything... its has a lot of inefficiencies.**

```python

class SortedTable:

	# packaging the key-value pair into one object
	class Record:
		def __init__(self, key, value):
			self.key = key
			self.value = value


	def __init__(self, cap=32):
		# this initializes a list of of capacity length with None
		self.the_table = [None for i in range(cap)]
		self.cap = cap

	def insert(self, key, value):
		if (self.search(key)!=None):
			return False

		if(len(self) == self.cap):
			# increase the capacity if list is full
			new_table = [None for i in range(self.cap*2)]
			for i in range(self.cap):
				new_table[i]=self.the_table[i]
			self.the_table = new_table
			self.cap *= 2


		self.the_table[len(self)]=self.Record(key,value)
		size = len(self)
		for i in range (0,size-1):
			for j in range(0,size-1-i):
				if(self.the_table[j].key>self.the_table[j+1].key):
					tmp=self.the_table[j]
					self.the_table[j]=self.the_table[j+1]
					self.the_table[j+1]=tmp
		return True

	def modify(self, key, value):
		i = 0
		while (i < len(self) and self.the_table[i].key != key):
			i+=1
		if(i==len(self)):
			return False
		else:
			self.the_table[i].value = value
			return True

	def remove(self, key):
		i = 0
		size = len(self)
		while (i < size and self.the_table[i].key != key):
			i+=1
		if(i==size):
			return False
		while(i+1 < size):
			self.the_table[i]=self.the_table[i+1]
			i+=1
		self.the_table[i] = None
		return True

	def search(self, key):
		i = 0
		size = len(self)
		while  i < size and self.the_table[i].key != key :
			i+=1
		if i==size:
			return None
		else:
			return self.the_table[i].value

	def capacity(self):
		return self.cap

	def __len__(self):
		i =0
		count = 0
		while(i < len(self.the_table)):
			if(self.the_table[i]!=None):
				count+=1
			i+=1
		return count

``` 

## Part B: Suggestions (4 marks)

Suggest 2 improvements you could make to the code that will improve its efficiency. State which function(s) would be improved by the suggested improvement.  Write up your suggestion into a2.md.   This is not a coding question.  You do not need to implement your suggestion.  A clear description of what you want to do is good enough.

**Which improvements counts and which do not**:
* You can't change the underlying data structure.  For example, "make it a hash table" would make it something different so that won't count.  Fundamentally it must use a sorted python list as the underlying data structure
* A change only counts once: "Do a selection sort instead of what is written in the __len__() function" and "Do a selection sort instead of what is written in the capacity() function" is just one suggestion not two. (note this suggestion is silly, and just used as an example)

## Part C Implementation of Linear Probing Hash Table two different ways (20 marks)

This section is to be implemented in **a2c.py**

When doing this coding portion of the assignment you can use:
* python lists (and functions to manipulate the list)
* python hash() function - don't write your own


A hash table places records based on a hash value that you get from a hash function.  We will use the built in hash function in python for this part of the assignment.  A hash function will return a really big number when given something to hash.  We will use this function to hash the key of our key-value pair (not the value, just the key).

Example usage:

```python
x = hash("hello world")     # x will be a number with many digits, possibly negative.
cap = 32	
idx = x % cap               # idx is guaranteed to be a value between 0 and 31 inclusive 
                            # because the mod operator guarantees that when you say x % n
                            # the result is always between 0 and n-1 inclusive
```

You will implement a linear probing hash table with tombstones (LinearProbingTS) and a linear probing table without tombstones (LinearProbingNoTS).  

### Resources:
* Linear probing table with Tombstones:  https://seneca-ictoer.github.io/data-structures-and-algorithms/F-Tables/linear-probing#method-2-tombstoning
* Linear probing table without Tombstones: https://seneca-ictoer.github.io/data-structures-and-algorithms/F-Tables/linear-probing#method-1
* Linear Probing table implementation video: https://web.microsoftstream.com/video/f0bb8b50-6629-4047-b7fa-b29b42c34505


### Member functions

For the LinearProbingTS and LinearProbingNoTS classes, the member functions are the same but they are implemented in different ways.  We will be looking at your code to ensure that they are correctly implemented as linear probing hash tables with and without tombstones.  Simply passing testing will not be enough.  If these do not conform to the described data structure, you will need to resubmit it with penalty.

---

```python
	def __init__(self, capacity=32):
```
The initializer for the table defaults the initial table capacity to 32.  It creates a list with capacity elements all initialized to None.

---


```python
	def insert(self, key, value):
```
This function adds a new key-value pair into the table. If a record with matching key already exists in the table, the function does not add the new key-value pair and returns False. Otherwise, function adds the new key-value pair into the table and returns True. If adding the new record causes the load factor to exceed 0.7, you must grow your table by doubling its capacity. Reminder load factor = number of items in table/capacity.

---

```python
	def modify(self, key, value):
```
This function modifies an existing key-value pair into the table. If no record with matching key exists in the table, the function does nothing and returns False. Otherwise, function changes the existing value into the one passed into the function and returns True

---

```python
	def remove(self, key):
```

This function removes the key-value pair with the matching key.  If no record with matching key exists in the table, the function does nothing and returns False.  Otherwise, record with matching key is removed and returns True

---

```python
	def search(self, key):
```

This function returns the value of the record with the matching key.  If no reocrd with matching key exists in the table, function returns None

---

```python
	def capacity(self):
```
This function returns the number of spots in the table.  This consists of spots available in the table.  

---

```python
	def __len__(self):
```

This function returns the number of Records stored in the table.

---



## Part D: Graph (14 marks)

When doing this coding portion of the assignment you can use:
* Python lists (and functions to manipulate the list)
* [Python Tuples](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)


A Graph data structure is a data structure used to represent a graph.  
See: https://seneca-ictoer.github.io/data-structures-and-algorithms/G-Graphs/representation

There are two ways to represent a graph.  It is up to you to choose the underlying data structure you will use.  To create an adajacency matrix, use a fixed sized list of fixed sized list (ie a 2D array).  To create an adjacency list use a fixed sized list of lists where the second dimension lists are initially empty python lists.


Your Graph class will have the following member functions:

```python
def __init__(self, number_of_verts)
```
This function creates a Graph object and initializes it to support **number_of_verts** vertices.

---

```python
def add_vertex(self)
```

This function adds an additional vertex to the graph.  (ie your graph now supports one more vertex than it had previously supported)

---

```python
def add_edge(self, from_idx, to_idx, weight=1)
```
* from_idx and to_idx are index values of two vertices
* weight is an optional 3rd value for the weight of the edge with a default weight of 1

If either of the vertices are invalid, or the edge already exists, this function does nothing and returns False.
Otherwise, this function will create a directed edge from the vertex from_idx to the vertex to_idx and return True 


---

```python
def num_edges(self)
```

This function returns the number of edges in the graph.

---

```python
def num_verts(self)
```
This function returns number of vertices in the grpah

---

```python
def has_edge(self, from_idx, to_idx)
```
* from_idx and to_idx are index values of two vertice
* this function returns True if there is an edge from vertex from_idx to vertex to_idx, otherwise it returns False
* if either of the vertices are invalid, function does nothing and returns False

---
```python
def edge_weight(self, from_idx, to_idx)
```
* from_idx and to_idx are index values of two vertice
* if either of the vertices are invalid, function does nothing and returns None
* if there is no edge from vertex from_idx to vertex to_idx function returns None
* Otherwise this function returns the weight for the edge from vertex from_idx to vertex to_idx

---
```python
def get_connected(self, v)
```
Finds all the vertices connected from v. That is all vertices that can be reached with a direct link starting from v.  This function returns an array of tuples where the first value of the tuple is the index of the vertex and the second value is the weight of the edge to that vertex.






## Part E: Reflection (5 marks):

This component is to be individually written and graded.  Please clearly put your name in the title of your reflection.
Complete this section in the a2.md file, please remember to put your name into the appropriate heading

In your reflection include the following:

1. Please detail what exactly **you** did for the assignment.
2. What was one thing **you** learned when doing this assignment?
3. What was its most challenging aspect and what did **you** do to overcome this challenge?

This answer is not about what your team did as a whole.  It is about what each team member individually contributed.


## Submission:

In order to for this assignment to be considered completed you must submit:
* the analysis for part A (placed in the a2.md)
* a successful run for parts C and D (green checks for parts C and D in actions)

Part B is optional for completion but failure to complete it will result in 0 for part B

Please make sure you follow the steps listed below fully

### What/How to submit

For part A to be considered complete, you must submit an updated a2.md with analysis of the listed functions. (part A is mandatory)

For part B, please place answers into a2.md

For part C to be considered completed, you must submit your a2c.py into the main branch of your a2 repository.  Your assignment is not complete unless it passes testing (look in the action tab for) a greencheckmark for assignment 2c and meet the specifications of the described data structure (ie submitting same code for both hashtables may pass testing but it is not complete as one of them will not meet the specification of the described data structure  (part C is mandatory)

For part D to be considered completed, you must submit your a2d.py into the main branch of your a2 repository.  Your assignment is not complete unless it passes testing (look in the action tab for) a greencheckmark for assignment 2d. (part D is mandatory)


### Resubmissions

* With the test verification there is very rarely a need to have you resubmit your program.  However, if there are many errors in your program or it misses the point entirely (you simply copied the sortedTable code into your hash table), you may be asked to resubmit your work.  Any work that is resubmitted, will receive a 50% penalty

## Grading Breaking

### Part A (analysis)

There are 6 functions/scenarios you are asked to analyze for part A and it is worth 12 marks.  The rubric for grading analysis is as follows:

 Criteria | Level 0 | Level 1 | Level 2 | Level 3 | Level 4 |
|---|---|---|---|---|---|
| Analysis | No analysis completed | Little to no explanation in analysis... arrives at final result as if by magic  | Lacks a significant component to analysis has one or more major errors or miscalculation within the analysis | Has minor errors or some minor missing steps in analysis  | Clearly laid out analysis with correct flow that shows how all mathematical expressions are obtained.  Clear and consistent usage of mathematical symbols.  Complete and clear count of operations |

Each function is judged independently.

### Part B (Improvements)

You get two marks for each improvement suggestion that isn't saying the same thing... so if you suggest doing one thing and that results in 3 function being faster, that isn't 3 different suggestions.  that is just one suggestion.  Make sure you have 2 distinct suggestions for improvements.  Improvements also cannot fundamentally change the data structure (it must stay a sorted array)

### Parts C and D (Implementation)

| Criteria | Level 0 | Level 1 | Level 2 | Level 3 | Level 4 |
|---|---|---|---|---|---|
| **Documentation - 20%** - Documentation is about Intention.  "This function is suppose to do" X.  It doesn't state HOW "we loop, then there is an if, then ..." - this is an example of what not to do.  It doesn't repeat code.  For each function ensure that it describe what it does (at a high level), what it accepts as arguments and any sort of restrictions (number must be positive for example) and what the function should return under what condition (returns true if found for example) |Almost no documentation of any type |only a few functions got documented and documentation tends to be code description as opposed to code intention. | many function documentation missing or severe lack of details for function description or documentation is done only at code level (within the code) and not as an overall intention| a few functions documentation missing. or function description comments lack some detail.  Over documentation.  documenting every line of code is not a good... let the code speak | For all functions state what parameters are (and any limitations, what return value is, what it does. |
| **Code Styling - 10%** Consistent styling is key.  This category describes things like indentation, consistent naming strategies, good variable names, not adding public member functions etc. | more than 5 cases of inconsistent or bad styling | 3 to 5 cases of inconsistent  or bad styling | 2 to 3 cases of inconsistent or bad styling functions | 1 case of inconsistent  or bad styling | Consistency is key. same variable name styling (snake_case is standard for python), same data member styling, same curly bracket positioning, correct and consistent indentation, good variable names | 
|**Correctness and Completeness of Code - 35%**.  This category generally describes errors in logic or missing functionality that may occur only in some cases.  This category also includes using things you are not suppose to use or not following specifications correctly | 4 or more errors | 3 errors | 2 errors - using something you are not suppose to use will count as two errors right away as it is a spec violation | 1 errors | all functions completed and correct |
| **Efficiency - 35%** - Anything that is completely off from optimal run time will always count as an instance of inefficiency.. thus if runtime can be O(n) and your code is written to O(n^2). Writing unnecessary code will also be counted as inefficient even if runtime is same.. for example copying array more than 1 time during a grow() operation | 4 or more instance of inefficiency | 3 instance of inefficiency | 2 instance of inefficiency| 1 instance of inefficiency | Function is as efficient as possible |

### Reflection Rubric

 Criteria | Level 0 | Level 1 | Level 2 | Level 3 | Level 4 |
|---|---|---|---|---|---|
| Reflection | No reflection written | Reflection has no specifics with generic statements that can apply to anything | Reflection lacks depth, only a brief description without any details | Reflection shows some depth with some descriptions.  It does not go far beyond the basic requirements | A clearly written reflection with clear thought that shows depth|
