# time - O(1), space - O(n)
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.mini = float('inf')

    def push(self, val: int) -> None:
        if val < self.mini:
            self.mini = val

        self.min_stack.append(self.mini)
        self.stack.append(val)
        
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        self.mini = float('inf') if not self.min_stack else self.min_stack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
