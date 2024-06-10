# prefixSum O(n + k)
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        rs = ans = 0
        dp = {0:1}
        for num in nums:
            rs = (rs + num)%k
            if rs in dp:
                ans += dp[rs]
                dp[rs] += 1
                continue
            dp[rs] = 1
        return ans
