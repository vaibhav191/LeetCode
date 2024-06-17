class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i, j = 0, int(math.sqrt(c))
        while i<=j:
            s = i**2 + j**2
            if s == c:
                return True
            elif s>c:
                j-=1
            elif s<c:
                i+=1
        return False
