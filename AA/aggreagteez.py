class aggregate:
    def __init__(self):
        self.stack = []
        self.totalOperations = 0
        self.cost = 0

    def push(self,element):
        self.stack.append(element)
        self.cost+=1
        self.totalOperations+=1
        print(f"Push: {element}")
        self.displayStack()
    
    def pop(self):
        if len(self.stack)==0:
            print("Stack Underflow")
        popped = self.stack.pop()
        self.cost+=1
        self.totalOperations+=1
        print(f"Pop: {popped}")
        self.displayStack()
    
    def multipop(self,k):
        print(f"Multipop start:")
        while self.stack and k>0:
            k-=1
            self.pop()
        print(f"multipop over.")
    
    def displayStack(self):
        print(self.stack,"\n")

stack = aggregate()
stack.push(10)
stack.push(20)
stack.push(30)
stack.pop()
stack.multipop(2)
print("Total Cost: ", stack.cost)
print("Total Operations: ", stack.totalOperations)
print("Amortized Cost per operation: ", stack.cost/stack.totalOperations)