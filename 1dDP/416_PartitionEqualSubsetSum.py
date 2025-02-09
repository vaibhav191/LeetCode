import copy
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        goal = total/2
        
        dp = set()
        dp.add(0)

        for i in range(len(nums) - 1, -1, -1):
            nextdp = copy.copy(dp)
            for t in dp:
                nextdp.add(t + nums[i])
            dp = (nextdp)
        return True if goal in dp else False
