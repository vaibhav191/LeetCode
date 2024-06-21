class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        l = 0
        r = minutes - 1
        
        #calculating the initial window
        customers_range_sum = sum(customers[l:r+1])
        current_satisfied_sum = 0
        current_satisfied_sum = sum(x*(not y) for x,y in zip(customers[l:r+1], grumpy[l:r+1]))
        
        #using max_diff encountered which will be the window where the minutes window will be applied
        #total_satisfied_customers track the total satisfied without the window of minutes applied
        max_diff = customers_range_sum - current_satisfied_sum
        total_satisfied_customers = current_satisfied_sum

        while l <= len(customers) - minutes:
            if l: # since precalculated, not triggering for l = 0
                customers_range_sum = customers_range_sum - customers[l-1] + customers[r]
                current_satisfied_sum = current_satisfied_sum - (customers[l-1]*(not grumpy[l-1])) + (customers[r]*(not grumpy[r]))
                total_satisfied_customers = total_satisfied_customers + (customers[r]*(not grumpy[r]))
            if customers_range_sum - current_satisfied_sum > max_diff: # check if difference is max encountered difference
                max_diff = customers_range_sum - current_satisfied_sum
            l += 1
            r += 1
            
        return total_satisfied_customers + max_diff

