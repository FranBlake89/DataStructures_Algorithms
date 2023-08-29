
# if you wish to use your sorted list from a1, copy and paste it here
# this is not the best way to do this but the test scripts are not
# designed to pick up an extra file. 

class LinearProbingTS:

	# This is a single record in a chaining hash table.  You can
	# change this in anyway you wish (including not using it at all)
	class Record:
		def __init__(self, key=None , value=None, status="empty"):
			self.key = key
			self.value = value
			self.status = status
	# You cannot change the function prototypes below.  Other than that
	# how you implement the class is your choice (but it must be a hash
	# table that use chaining for collision resolution)

	def __init__(self, cap=32):
		self.table = [None] * cap
		self.size = 0

	def insert(self,key, value):
		new_rec = self.Record(key,value,"used")
		#print(' size {} cap: {}'.format( self.size, self.capacity() ) )
		hash_idx = self._hash_code(key)
		
		while self.table[hash_idx] is not None and self.table[hash_idx].key != key:
			hash_idx = (hash_idx + 1) % self.capacity()
		
		if self.table[hash_idx] is None:
			self.table[hash_idx] = new_rec
			self.size += 1
			#check whether resizing is necessary after adding
			load_factorial = self.size / self.capacity()
			if load_factorial >= 0.7:
				self.resize_table()
			return True
		
		return False


	def modify(self, key, value):
		cnt = 0
		index = self._hash_code(key)

		if cnt > self.capacity():
			return False
		
		while self.table[index] is not None:
			if self.table[index].status != "deleted" and self.table[index].key == key:
				self.table[index].value = value
				return True
			index = (index + 1) % self.capacity()
			cnt += 1
		
		return False

	def remove(self, key):
		cnt = 0
		index = self._hash_code(key)

		if cnt > self.capacity():
			return False
		
		while self.table[index] is not None:
			if self.table[index].status != "deleted" and self.table[index].key == key:
				self.table[index].status = "deleted"
				self.table[index].key = None
				self.table[index].value = None
				self.size -= 1
				return True
			index = (index + 1) % self.capacity()
			cnt +=1

		return False

	def search(self, key):
		counter = 0
		index = self._hash_code(key)
		
		if counter > self.capacity():
			return None
			
		while self.table[index] is not None:
			if self.table[index].status != "deleted" and self.table[index].key == key:
				return self.table[index].value # Return the value of the matching key
			index = (index + 1) % self.capacity()
			counter += 1

		return None  # No record with matching key found, return None


	def capacity(self):
		return len(self.table)
	
	def resize_table(self):
		old_table = self.table
		#print('before',self.capacity())
		double_size = self.capacity() * 2
		self.table =  [None] * double_size
		self.size = 0
		
		for rec in old_table:
			if rec and rec != "deleted":
				self.insert(rec.key, rec.value)
				#print('after:',self.capacity())

	def _hash_code(self, key):
		return hash(key) % self.capacity()
	
	def __len__(self):
		return self.size
		
	# comment: This function returns the number of Records stored in the table.


class LinearProbingNoTS:
	"""
	h
	"""
	class Record:
		"""
		h
		"""
		def __init__(self, key=None, value=None):
			self.key = key
			self.value = value


	def __init__(self, cap=32):
		# Initialize the hash table with a given capacity
		self._cap = cap
		self.size = 0
		self.table = [None] * self._cap

	def _hash(self, key):
		# Compute the hash value for a given key
		return hash(key) % self.capacity()

	def _probe(self, index):
		# Perform linear probing to find the next available index
		return (index + 1) % self.capacity()

	def resize(self):
		old_table = self.table
		#print('before',self.capacity())
		double_size = self.capacity() * 2
		self.table =  [None] * double_size
		self.size = 0

		for rec in old_table:
			if rec and rec != "deleted":
				self.insert(rec.key, rec.value)
			#print('after:',self.capacity())

	def insert(self, key, value):
		"""
		h
		"""
		# Insert a key-value pair into the hash table
		new_rec = self.Record(key, value)
		index = self._hash(key)

		while self.table[index] is not None and self.table[index].key != key:
			index = self._probe(index)

		if self.table[index] is None:
			self.table[index] = new_rec
			self.size += 1
			#check whether resizing is necessary after adding
			load_factorial = self.size / self.capacity()
			if load_factorial >= 0.7:
				self.resize()
			return True

		return False

	def modify(self, key, value):
		# Modify the value for an existing key in the hash table
		index = self._hash(key)
		count = 0
		if count > self.capacity():
			return False

		while self.table[index] is not None:
			if self.table[index].key == key:
				self.table[index].value = value
				return True
			index = self._probe(index)
			count += 1

		# If the key is not found, raise a KeyError
		return False

	def remove(self, key):
		# Remove a key-value pair from the hash table
		index = self._hash(key)

		while self.table[index] is not None:
			if self.table[index].key == key:
				# Set the key and value to None to mark the index as empty
				self.table[index].key = None
				self.table[index].value = None
				self.size -= 1
				
				count = 0
				removed_idx = index
				next_idx = self._probe(index)
				
				while self.table[next_idx] is not None:
				    hash_idx = self._hash(self.table[next_idx].key)
				    
				    if hash_idx <= removed_idx and hash_idx < next_idx :
				        self.table[removed_idx] = self.table[next_idx]
				        self.table[next_idx] = None
				        removed_idx = next_idx
				    next_idx = self._probe(next_idx)
				return True
			index = self._probe(index)

		return False

	def search(self, key):
		# Search for a key and return the associated value
		index = self._hash(key)

		while self.table[index] is not None:
			if self.table[index].key == key:
				return self.table[index].value
			index = self._probe(index)

		# If the key is not found,return None
		return None

	def capacity(self):
		# Return the current capacity of the hash table
		return len(self.table)

	def __len__(self):
		# Return the number of elements in the hash table
		return self.size
