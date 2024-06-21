class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfied = [x if y==0 else 0 for x,y in zip(customers,grumpy)]
        l = 0
        r = minutes - 1
        customers_range_sum = sum(customers[l:r+1])
        current_satisfied_sum = sum(satisfied[l:r+1])
        max_diff = customers_range_sum - current_satisfied_sum

        while l <= len(customers) - minutes:
            if l:
                customers_range_sum = customers_range_sum - customers[l-1] + customers[r]
                current_satisfied_sum = current_satisfied_sum - satisfied[l-1] + satisfied[r]
            if customers_range_sum - current_satisfied_sum > max_diff:
                max_diff = customers_range_sum - current_satisfied_sum
            
            l += 1
            r += 1
            
        return sum(satisfied) + max_diff
