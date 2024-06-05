from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        # method 2 using deque
        stack = deque()
        Map = {')':'(', ']':'[', '}':'{'}
        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack.pop()!=Map[c]:
                return False
        return not stack
