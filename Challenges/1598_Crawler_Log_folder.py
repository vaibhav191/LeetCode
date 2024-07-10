class Solution:
    def minOperations(self, logs: List[str]) -> int:
        level = 0
        for step in logs:
            if step == '../':
                if level:
                    level -= 1
                continue
            if step == './':
                continue
            level += 1
        return level
