class Stack:
    def __init__(self):
        seznam = self.seznam = []

    def push(self, prvek):
        self.seznam.append(prvek)

    def IsEmpty(self):
        if len(self.seznam) == 0:
            return True
        else:
            return False
        
    def pop(self):
        if self.IsEmpty():
            return None
        else:
            posledni_prvek = self.seznam.pop()
            return posledni_prvek

    def peek(self):
        if self.IsEmpty():
            return None
        else:
            return self.seznam[-1]
        
    def __str__(self):
        return str(self.seznam)
        
zasobnik = Stack()
zasobnik.push(1)
print(zasobnik)

    







    

