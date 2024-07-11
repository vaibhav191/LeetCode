# Wormhole
class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        bracs_indices = []
        pair = [0]*n
        for i in range(n):
            if s[i] == '(':
                bracs_indices.append(i)
            if s[i] == ')':
                j =bracs_indices.pop()
                pair[i], pair[j] = j, i
        ans = []
        cur_index = 0
        direction = 1
        while cur_index < n:
            if s[cur_index] == '(' or s[cur_index] == ')':
                cur_index = pair[cur_index]
                direction = -direction
            else:
                ans.append(s[cur_index])
            cur_index += direction
        return ''.join(ans)
