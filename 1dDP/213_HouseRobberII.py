# On time, O1 space
class Solution:
    def rob(self, nums: List[int]) -> int:
        def house_robber(nums):
            r1, r2 = 0, 0
            for n in nums:
                temp = max(r1 + n, r2)
                r1 = r2
                r2 = temp
            return r2
        return max(nums[0], house_robber(nums[1:]), house_robber(nums[:-1]))
    
        
