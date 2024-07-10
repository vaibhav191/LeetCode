class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        count = numBottles
        num_empty = numBottles
        while (num_empty)//numExchange > 0:
            count += num_empty//numExchange
            num_empty = num_empty//numExchange + num_empty % numExchange
        return count
