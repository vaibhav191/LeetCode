class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_count = Counter(nums1)
        ans = []
        for num in nums2:
            if num in nums1_count and nums1_count[num]:
                ans.append(num)
                nums1_count[num] -= 1
        return ans
