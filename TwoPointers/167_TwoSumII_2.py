#beats 99.43%
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while numbers[l] + numbers[r] != target:
            sum_ = numbers[l] + numbers[r]
            if sum_ < target:
                l = l+1
            elif sum_ > target:
                r = r-1
        return [l+1, r+1]
