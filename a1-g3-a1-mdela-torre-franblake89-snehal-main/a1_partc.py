from a1_partb import SetList

class DisjointSet:
	def __init__(self):
		self.sets = {}
		self.size = {}
		self.num_elements = 0
		self.num_sets = 0

	"""
	This function creates a new SetList that only contains
	one Node which stores the element as a data and stores 
	a new entry to the dictionary.
	The dictionary uses the element as the key and a reference to the node as its value
	"""
	def make_set(self, element):
		if element in self.sets:
			return False
		new_set = SetList()
		new_node = new_set.make_set(element)
		self.sets[element] = new_node
		self.size[element] = 1
		self.num_elements += 1
		self.num_sets += 1 
		return True

	# The function returns the number of existing SetList
	def get_num_sets(self):
		return self.num_sets
	
	# This function returns the size of the set that where the element is contained
	def get_set_size(self,element):
		if element in self.sets:
			return self.size[self.find_set(element)]
		return 0

	# This function returns the number of elements inside the dictionary (sets)
	def __len__(self):
		return self.num_elements

	"""
	This function returns the data from the first node of the SetList
	SetList object has an existing function (representative()) that you could
	use to achieve what the function wants.
	"""
	def find_set(self, element):
		if element not in self.sets:
			return None
		if self.sets[element].get_data() != element:
			self.sets[element] = self.find_set(self.sets[element].get_data())
		return self.sets[element].get_set().representative()

	"""
	The function returns false for the following conditions:
	1. element1 and element2 does not match any keys
	2. element1 and element2 belong to the same SetList
	If these are not true, then it will transfer the smallest SetList to the larger set
	then it returns True
	"""
	def union_set(self, element1, element2):
		if element1 not in self.sets or element2 not in self.sets:
			return False

		set1 = self.sets[element1].get_set()
		set2 = self.sets[element2].get_set()

		if set1 is set2:
			return False
		
		# Swap sets to merge the smallest set to the larger one
		if len(set1) < len(set2):
			set1, set2 = set2, set1
		
		# Update the size of the set
		self.size[set1.representative()] += self.size[set2.representative()]
		self.size[set2.representative()] = self.size[set1.representative()] # Stores the same size with set1 after merging

		set1.union_set(set2)
		self.num_sets -= 1

		return True

		

