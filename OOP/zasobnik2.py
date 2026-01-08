class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, cislo):
        if self.IsEmpty():
            novy_vrchol = Node(cislo)
            self.top = novy_vrchol
        else:
            novy_vrchol = Node(cislo)
            novy_vrchol.next = self.top
            self.top = novy_vrchol

    def pop(self):
        if self.IsEmpty():
            return None
        elif self.top.next is None:
            value = self.top.value
            self.top = None
            return value
        else:
            value = self.top.value
            self.top = self.top.next
            return value
    
    def IsEmpty(self):
        if self.top is None:
            return True 
        else:
            return False