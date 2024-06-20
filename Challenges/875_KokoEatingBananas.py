class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        low = 1
        high = float('-inf')
        for pile in piles:
            if pile>high:
                high = pile
        min_mid = float('inf')
        while low <= high:
            mid = (low+high)//2
            hrs = sum([ceil(pile/mid) for pile in piles])
            if hrs>h:
                low = mid + 1
            elif hrs <= h:
                high = mid - 1
                min_mid = min(min_mid, mid)
        return min_mid
