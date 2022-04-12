class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

        
    def insert(self, index, value):
        pass

    def pop(self, index):
        pass

    def remove(self, value):
        prev = None
        curr = self.head
        while curr:
            if curr.value == value:
                if prev: 
                    prev.next = curr.next
                else: 
                    self.head = curr.next
                break
            prev, curr = curr, curr.next


    def index(self, value):
        pass

    def count(self, value):
        pass

    def sort(self, reverse=False):
        pass

    def reverse(self):
        pass

    def clear(self):
        pass

    def copy(self):
        pass

    def __str__(self):
        pass

    def __len__(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count


    def __iter__(self):
        curr = self.head
        while curr:
            yield curr.value
            curr = curr.next


    def __getitem__(self, index):
        curr = self.head
        for _ in range(index):
            try:
                curr = curr.next
            except AttributeError:
                # tbc: error handling
                print("Index Error: LinkedList index out of range")
                return
        return curr.value

    def __setitem__(self, index, new_value):
        pass


    def __contains__(self, value):
        curr = self.head
        while curr:
            if curr.value == value:
                return True
            curr = curr.next
        return False


    def __add__(self, other):
        # tbc: modifies l1
        if not self.head:
            self.head = other.head
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = other.head
        return self
