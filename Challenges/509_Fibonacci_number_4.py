#Benit's formula for fibo
#F(n) = (GR^n - (1-GR)^n)/sqrt(5)
#GR = Golden Ratio = (1+sqrt(5))/2
from math import sqrt
class Solution:
    def __init__(self):
        self.phi = (1 + math.sqrt(5)) / 2
        self.psi = (1 - math.sqrt(5)) / 2
        
    def fib(self, n: int) -> int:
        return round((self.phi**n - self.psi**n) / sqrt(5))
