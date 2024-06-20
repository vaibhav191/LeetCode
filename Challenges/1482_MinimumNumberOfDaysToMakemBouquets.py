class Solution:
    def validBouquets(bloomDay,mid, k):
        count = 0
        bouquets = 0
        for day in bloomDay:
            if day<=mid:
                count += 1
            else:
                count = 0
            if count == k:
                bouquets += 1
                count = 0
        return bouquets

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k>len(bloomDay):
            return -1
        
        start, end = 0, max(bloomDay)
        min_days = -1

        while start <= end:
            mid = (start + end)//2
            no_of_bouquets = Solution.validBouquets(bloomDay, mid, k)
            
            if no_of_bouquets >= m:
                min_days = mid
                end = mid - 1
            else:
                start = mid + 1
        return min_days
