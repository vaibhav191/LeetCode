class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums = sorted(nums)
        def backtrack(i, subset):
            if i == len(nums):
                ans.append(subset.copy())
                return
            
            # include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
            # don't include nums[i]
            while (i < (len(nums) - 1)) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)
            
        backtrack(0, [])
        return ans
