class Queue:
    def __init__(self):
        self.seznam = []

    def enqueue(self, prvek):
        self.seznam.append(prvek)

    def IsEmpty(self):
        if len(self.seznam) == 0:
            return True
        else:
            return False
        
    def dequeue(self):
        if self.IsEmpty():
            return None
        else:
            self.seznam.pop(0)
    
    def peek(self):
        return self.seznam[-1]
    
    def __str__(self):
        return str(self.seznam)
    
zasobnik = Queue()
zasobnik.enqueue(1)
zasobnik.enqueue(2)
zasobnik.enqueue(3)
zasobnik.enqueue(4)
zasobnik.dequeue()
print(zasobnik.peek())



