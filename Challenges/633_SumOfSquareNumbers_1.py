# O sqrt.c. logc
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(0, int((c)**0.5)+1):
            b = (c-(i**2))**0.5
            if int(b) == b:
                    return True
        return False
