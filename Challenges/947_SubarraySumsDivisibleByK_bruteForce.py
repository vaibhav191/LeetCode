# brute force O(n^2)
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = []
        for i in range(len(nums)):
            subSum = 0
            for j in range(i, len(nums)):
                subSum += nums[j]
                if subSum % k == 0:
                    print(i, j)
                    res.append(nums[i : j + 1])
        return len(res)

