class Stack:
    def __init__(self,size) -> None:
        self.list = []
        self.maxSize = size
    
    def __str__(self) -> str:
        values = self.list[::-1]
        values = [str(x) for x in values]
        return '\n'.join(values)

    
    def isEmpty(self):
        if self.list == []:
            return True
        return False
    
    # isFull
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False

    def peek(self):
        if not self.isEmpty():
            data = self.list[-1]
            return data
    
    #  Push
    def push(self, value):
        if self.isFull():
            return "The stack is full"
        else:
            self.list.append(value)
            return "The element has been successfully inserted"
    # Pop
    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.list.pop()


customStack = Stack(4)
print(customStack.isEmpty())
print(customStack.isFull())
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
print(customStack)
