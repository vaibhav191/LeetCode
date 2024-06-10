#O(n)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumMap = {0:1}
        subsum = 0
        count = 0
        for i in range(len(nums)):
            subsum += nums[i]
            diff = subsum - k
            if (diff) in sumMap:
                count+=sumMap.get(diff, 1)
            sumMap[subsum] = sumMap.get(subsum, 0) + 1
            
        return count
