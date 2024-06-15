#O(n+max)
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        steps = 0
        maxn, minn = max(nums), min(nums)
        arr = [0]*(maxn+len(nums))
        for i in range(len(nums)):
            arr[nums[i]] += 1
        for i in range(minn, len(arr)):
            if arr[i] > 1:
                arr[i+1] += arr[i] - 1
                steps += arr[i] - 1
                arr[i] = 1
        # print(arr)
        return steps

