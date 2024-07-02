class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count_odds = 0
        for num in arr:
            if num%2 == 1:
                count_odds += 1
            else:
                count_odds = 0
            if count_odds == 3:
                return True
        return False
