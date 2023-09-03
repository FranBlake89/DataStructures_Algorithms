#
# Author: Francisco Castillo
# Student Number:
#
# Place the code for your lab 3 here.  Read the specs carefully.  
# Function name must be exactly as provided.  
# Names of variables and parameters can be whatever you wish it to be
#
# To test, run the following command :
#     python test_lab3.py
#

def factorial(number):
	if number ==0:
		return 1
	else:
		return number * factorial(number-1)


def linear_search(list, key):
	return linear_search_recursive(list, key, len(list) - 1)


def binary_search(list, key):
	return binary_search_recursive(list, key, 0, len(list) -1)  

def linear_search_recursive(list, key, index):
	if index < 0:
		return -1
	elif list[index] == key:
		return index
	else:
		return linear_search_recursive(list, key, index - 1)

def binary_search_recursive(lst, key, low, high):
	if low > high:
		return -1  # Key not found

	mid = (low + high) // 2

	if lst[mid] == key:
		return mid  # Key found at index mid
	elif lst[mid] > key:
		return binary_search_recursive(lst, key, low, mid - 1)  # Search in the left half
	else:
		return binary_search_recursive(lst, key, mid + 1, high)  # Search in the right half