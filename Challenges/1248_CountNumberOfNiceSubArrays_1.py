class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [1 if x % 2 == 1 else 0 for x in nums]
        def sum_goal_k(nums, goal):
            start, current_sum, total_count = 0, 0, 0
            for end in range(len(nums)):
                current_sum += nums[end]
                while start<=end and current_sum > goal:
                    current_sum -= nums[start]
                    start += 1
                
                total_count += end - start + 1
            return total_count
        return sum_goal_k(nums, k) - sum_goal_k(nums, k-1)

