class Stack():
    def __init__(self):
        self.table = []
        self.top = -1
    def push(self, x):
        self.table.append(x)
        self.top+=1
    def pop(self):
        self.table.pop()
        self.top-=1
    def display(self):
        for i in self.table:
            print(i, end=' ')
        print()

dynamic_array = Stack()
dynamic_array.push(1)
dynamic_array.push(2)
dynamic_array.push(3)
dynamic_array.push(4)
dynamic_array.push(5)
dynamic_array.display()
dynamic_array.pop()
dynamic_array.display()
dynamic_array.pop()
dynamic_array.display()