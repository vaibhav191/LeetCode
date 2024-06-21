class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def sumByDivisor(nums, divisor):
            return sum([ceil(x/divisor) for x in nums])
        l = 1
        r = max(nums)
        min_divisor = float('inf')
        while l<=r:
            mid = (l + r)>>1
            s = sumByDivisor(nums, mid)
            # print(mid, s, min_divisor)
            if s>threshold:
                l = mid + 1
            elif s <= threshold:
                r = mid - 1
                min_divisor = min(min_divisor, mid)
        return min_divisor
