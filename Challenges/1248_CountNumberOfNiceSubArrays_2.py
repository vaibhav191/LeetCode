class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [1 if x % 2 == 1 else 0 for x in nums]
        
        start, total_count, current_sum, prefix_zeroes = 0, 0, 0, 0

        for end in range(len(nums)):
            current_sum += nums[end]

            while start<end and (current_sum > k or nums[start] == 0):
                if nums[start] == 0:
                    prefix_zeroes += 1
                else:
                    prefix_zeroes = 0
                current_sum -= nums[start]
                start += 1
            if current_sum == k:
                total_count += 1 + prefix_zeroes

        return total_count
