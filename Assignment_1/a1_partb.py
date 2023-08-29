"""
SetList Module

The SetList class, which simulates a list with set operations, is implemented in this module.
It offers techniques for building sets, carrying out union operations, locating nodes, and obtaining representative data.


Author: Snehal (165189218)
Date of completion: 15th JUNE 2023
"""

class SetList:
    class Node:
        def __init__(self, data=None, set_list=None, next_node=None, prev_node=None):
            """
            Initializes a Node instance.

            """
            self.data = data
            self.set_list = set_list
            self.next_node = next_node
            self.prev_node = prev_node

        def get_data(self):
            """
            Returns the data which is stored in node.
            """
            return self.data

        def get_next(self):
            """
            In the SetList,Returns the reference to the next node.
            """
            return self.next_node

        def get_previous(self):
            """
            Returns the reference to the previous node 
            """
            return self.prev_node

        def get_set(self):
            """
            Returns the reference self.set_list
            """
            return self.set_list

    def __init__(self):
        """
        creates an instance of a SetList with empty head and tail nodes.

        """
        self.head = None
        self.tail = None
        self.size = 0

    def get_front(self):
        """
        Returns the reference self.head


        """
        return self.head

    def get_back(self):
        """
        Returns the reference self.tail
        """
        return self.tail

    def make_set(self, data):
        """
        if the SetList is empty, creates a new node and returns its reference.

        data: The data that will be saved in the new node.

        Returns:
            Node: A mention of the just formed node.
                  None if the SetList contains any items.

        """
        if self.head is not None:
            return None
        
        new_node = self.Node(data, self)
        self.head = new_node
        self.tail = new_node
        self.size += 1
        return new_node

    def union_set(self, other_set):
        """
        combines two instances of the SetList.

        Args: another SetList object instance named other_set.


        Returns: int: The amount of transferred elements.

        """
        current = other_set.head
        while current is not None:
            current.set_list = self
            current = current.get_next()
            self.size += 1
            other_set.size -= 1
        if self.tail is not None:
            self.tail.next_node = other_set.head
            other_set.head.prev_node = self.tail
            self.tail = other_set.tail
        else:
            self.head = other_set.head
            self.tail = other_set.tail
        
        other_set.head = None
        other_set.tail = None
        return self.size

    def find_data(self, data):
        """
        Locates a node in the SetList that has the required data.

         Args: data: The data that will be looked for.

         Returns: Node: Reference to the node, if it was located.
                  None if there isn't a node containing the required info.
        """
        current = self.get_front()
        while current is not None:
            if current.data == data:
                return current
            current = current.get_next()
        return None

    # The function returns the node that is at the front of the SetList
    def representative_node(self):
        if self.head is None:
            return None
        return self.head

    def representative(self):
        rep = self.representative_node()
        if rep is None:
            return None
        return rep.get_data()
    
    def __len__(self):
        return self.size