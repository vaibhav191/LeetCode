class Solution:
    def minOperations(self, logs: List[str]) -> int:
        level = deque()
        for step in logs:
            if step == '../':
                if level:
                    level.pop()
                continue
            if step == './':
                continue
            level.append(step)
        return len(level)
