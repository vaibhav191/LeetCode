class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        side = time//(n-1)
        if side % 2 == 1:
            return n - (time%(n-1))
        return time%(n-1) + 1
