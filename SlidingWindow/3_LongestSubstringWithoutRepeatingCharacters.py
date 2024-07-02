class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, ans = 0, 0, 0
        cur_elements = set()
        while r<=len(s) - 1:
            if s[r] in cur_elements:
                while s[r] in cur_elements:
                    cur_elements.remove(s[l])
                    l += 1
            cur_elements.add(s[r])
            ans = max(ans, len(cur_elements))
            r += 1
        return ans
