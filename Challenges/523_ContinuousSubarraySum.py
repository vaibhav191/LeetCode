#O(n)
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dicMap = {0: -1}
        Sum = 0
        for i, num in enumerate(nums):
            Sum += num
            rem = Sum % k
            if rem not in dicMap:
                dicMap[rem] = i
            elif i-dicMap[rem]>1:
                return True
        return False
