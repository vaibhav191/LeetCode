# from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        # method one using maps and list as a stack
        Map = {')':'(','}':'{',']':'['}
        stack = []
        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or Map[c] != stack[-1]:
                return False
            stack.pop()
        return True if not stack else False

