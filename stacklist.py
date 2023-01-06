class Stack:
    def __init__(self) -> None:
        self.list = []
    
    def __str__(self) -> str:
        values = self.list[::-1]
        values = [str(x) for x in values]
        return '\n'.join(values)
    @property
    def isEmpty(self):
        if self.list == []:
            return True
        return False
    
    def push(self,value):
        self.list.append(value)
    
    def pop(self):
        if not self.isEmpty:
            data = self.list.pop()
            return data
        print("stack is empty")

    def delete(self):
        self.list = []

customstack = Stack()
customstack.push(1)
customstack.push(2)
customstack.push(3)
customstack.push(4)
print(customstack)
print(customstack.pop())
print(customstack)