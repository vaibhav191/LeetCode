class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l = 0
        r = len(nums) - 1
        m = l + (r - l)//2
        min_mid = nums[m]
        
        while l<=r:
            # if nums[r] < nums[m] then we need to scan right side for the smaller portion
            if nums[r] < nums[m]:
                l = m + 1
            # else the smaller portion is to the left
            else:
                r = m - 1
            m = l + (r - l)//2
            min_mid = min(min_mid, nums[m])
        return min_mid
