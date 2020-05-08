class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """    
        self.stack = []
        self.MinStack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.MinStack) == 0 or x <= self.MinStack[-1]:# first element could be null, excuting from left to rigt
            self.MinStack.append(x)

    def pop(self) -> None:
        if len(self.stack):  # len(self.stack) = 0 = False others like 1,2,3... is True
            if self.stack.pop() == self.MinStack[-1]:
                self.MinStack.pop()        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.MinStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
