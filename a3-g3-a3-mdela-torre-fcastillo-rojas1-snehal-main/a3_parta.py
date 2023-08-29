# A class for a min heap
class MinHeap:
    
    def __init__(self, arr=[]):
        self.heap = arr[:] # making self.heap unaffected by any modifications to arr
        self.heapify() # build a min heap in place

    def insert(self, element):
        self.heap.append(element)
        
        index = len(self.heap) - 1 #Start with the last element
        parent_idx = (index - 1) // 2 

        #Element is swapped with the parent if the value on the child(index) is smaller
        while index > 0 and self.heap[index] < self.heap[parent_idx]:
            self.heap[index], self.heap[parent_idx] = self.heap[parent_idx], self.heap[index]
            index = parent_idx
            parent_idx = (index - 1) // 2

    
    def get_min(self):
        if self.is_empty():
            return None
        return self.heap[0]
    
    # Returns the smallest value while also removing it
    def extract_min(self):
        if self.is_empty():
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        #Restructures the heap to maintain the order 
        #by calling heapify_down starting from the root
        min = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)

        return min

    def is_empty(self):
        return len(self.heap) == 0

    def __len__(self):
        return len(self.heap)

    def heapify(self):
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self.heapify_down(i)

    def heapify_down(self, parent):
        size = len(self.heap)
        smallest = parent
        left = 2 * parent + 1
        right = 2 * parent + 2
        
        #Left child is smaller than the parent
        if (left < size) and (self.heap[left] < self.heap[parent]):
            smallest = left
        
        #Right child is smaller than the left child and the parent
        if (right < size) and (self.heap[right] < self.heap[smallest]):
            smallest = right
        
        if smallest != parent:
            self.swap(parent, smallest)
            self.heapify_down(smallest)
            
    
    def swap(self, pos1, pos2):
        self.heap[pos1], self.heap[pos2] = self.heap[pos2], self.heap[pos1]
        

