class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


#Linked List 
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.lenght = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.lenght += 1
        return True

    def pop(self):
        if self.lenght == 0:
            return None

        temp = self.head
        pre = self.head

        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.lenght -= 1

        if self.lenght == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.lenght == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.lenght += 1
        return True

    def pop_first(self):
        if self.lenght == 0:
            return None

        temp = self.head.next
        self.head = None
        self.head = temp
        self.lenght -= 1

        if self.lenght == 0:
            self.tail = None

    def get(self, index):
        if index < 0 or index >= self.lenght:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.lenght:
            return None
        if index == 0:
            return self.prepend
        if index == self.lenght:
            return self.append
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        lenght += 1
        return True

    def remove(self, index):
        if index < 0 or index > self.lenght:
            return None
        if index == 0:
            return self.pop_first
        if index == self.lenght - 1:
            return self.pop
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        lenght -= 1

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.lenght):
            after = temp.next
            temp.next = before
            before = temp
            temp = after



class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.value = value
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next
    
    
    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        
    def pop(self):
        if self.height == 0:
            return None
        else:
            temp = self.top
            self.top = self.top.next
            temp = None
        self.height -= 1



class Queue:
    
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            temp = self.first
            self.first = self.first.next
            temp.next = None
        self.length += 1
        
            