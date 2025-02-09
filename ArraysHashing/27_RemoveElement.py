# O(n)-time O(1) - space
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        last_index = len(nums) - 1
        i = 0
        while i <= last_index:
            if nums[i] == val:
                nums[i] = nums[last_index]
                last_index -= 1
                continue
            i += 1
        return i
