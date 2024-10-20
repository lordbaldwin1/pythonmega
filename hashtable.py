class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    # find index with _hash()
    # if !self.table[index] create new node
    def insert(self, key, value):
        index = self._hash(key)
        if (self.table[index] == None):
            self.table[index] = Node(key, value)
            self.size += 1
        # else we need to iterate through linked list
        # see if key exists and update its value if it does
        # otherwise, create new node at head of list
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            new_node = Node(key, value)
            new_node.next = self.table[index]
            self.table[index] = new_node
            self.size += 1
    
    # find index in array where key should be
    # if self.table[index] == None, it does not exits
    # otherwise traverse the list and check for key, display value
    def search(self, key):
        index = self._hash(key)
        if self.table[index] == None:
            print("Key not found")
            return
        else:
            current = self.table[index]
            while current:
                if current.key == key:
                    print("Key", current.key, "found at index", index)
                    print("Value of key", current.value)
                    return current.value
                current = current.next
            print("Key", key, "not found")
        return
    
    # find index where key, value pair should be
    # if None at index, return
    # else, loop through linked list hold onto previous Node
    # move forward with current, if current.key == key
    # set prev.next = current.next
    def remove(self, key):
        index = self._hash(key)
        if self.table[index] == None:
            print("No value to remove")
            raise KeyError(key)
        current = self.table[index]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                    print(key, "removed")
                    return
                else:
                    current = None
            prev = current
            current = current.next
        print("Value not found")
        raise KeyError(key)
        


            


table = HashTable(10)
table.insert(1, 5)
value = table.search(1)
table.remove(1)
value = table.search(1)
print(value)
# print(table)