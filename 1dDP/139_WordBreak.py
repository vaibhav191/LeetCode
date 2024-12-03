class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        minw = float('inf')
        for w in wordDict:
            minw = min(len(w), minw)

        for i in range(len(s) - 1, -1, -1):
            if i + minw > len(s):
                continue
            for w in wordDict:
                if i + len(w) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break
        
        return dp[0]
