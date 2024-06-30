class Solution: 
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        current_sum, prefixZeroes, start = 0, 0, 0
        total_count = 0

        for end in range(len(nums)):
            current_sum += nums[end]

            while start< end and (current_sum> goal or nums[start] == 0):
                if nums[start] == 0:
                    prefixZeroes += 1
                else:
                    prefixZeroes = 0
                current_sum -= nums[start]
                start += 1
            if current_sum == goal:
                total_count += 1 + prefixZeroes
        
        return total_count
