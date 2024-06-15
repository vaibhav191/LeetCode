# nlogn
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        steps = 0
        nums = sorted(nums)
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                nums[i] += 1
                steps += 1
            elif nums[i-1] > nums[i]:
                steps += nums[i-1] - nums[i] + 1
                nums[i] = nums[i-1] + 1
        # print(nums)
        return steps
