class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def days_taken(weights, capacity):
            cur_weight = 0
            days = 0
            for weight in weights:
                cur_weight += weight
                if cur_weight == capacity:
                    days += 1
                    cur_weight = 0
                elif cur_weight > capacity:
                    days += 1
                    cur_weight = weight    
            if cur_weight:
                days += 1
            return days
        if days == 1:
            return sum(weights)
        l_weight = max(weights)
        r_weight = 50000
        min_weight = float('inf')

        while l_weight<=r_weight:
            mid = (l_weight + r_weight)>>1
            count = days_taken(weights, mid)
            if count > days:
                l_weight = mid + 1
                # min_weight = min(min_weight, mid)
            elif count<=days:
                r_weight = mid - 1
                min_weight = min(min_weight, mid)
        return min_weight

