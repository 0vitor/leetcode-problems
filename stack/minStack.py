class MinStack:

    def __init__(self):
        self.stack = []
        self.min_values = []
        
    def push(self, val: int) -> None:

        if len(self.stack):
            current_min = self.min_values[-1]
            if current_min > val:
                self.min_values.append(val)
            else:
                self.min_values.append(current_min)
        else:
            self.min_values.append(val)

        self.stack.append(val)

    def pop(self) -> None:
        if len(self.stack):
            self.stack.pop()        
            self.min_values.pop()        

    def top(self) -> int:
        if len(self.stack):
            return self.stack[-1]
        return None
        

    def getMin(self) -> int:
        if len(self.stack):
            return self.min_values[-1]
        return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
