from collections import deque
class MinStack:

    def __init__(self):
        self.stack = deque()
        self.Min = None
    def push(self, val: int) -> None:
        if self.Min is None:
            self.Min = val
        if val<self.Min:
            self.Min = val
        self.stack.append([val, self.Min])
        # print(self.stack)
        

    def pop(self) -> None:
        self.stack.pop()
        if not self.stack:
            self.Min = None
        else:
            self.Min = self.stack[-1][1]
        
    def top(self) -> int:
        # print(self.stack)
        return self.stack[-1][0]

    def getMin(self) -> int:
        # print(self.stack)
        return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
