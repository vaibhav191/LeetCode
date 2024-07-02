def permutes(s):
            if len(s) == 1:
                return [s]
            ans = []
            for i in range(len(s)):
                remaining_chars = s[:i] + s[i+1:]
                for perm in permutes(remaining_chars):
                    ans.append(s[i] + perm)
            return ans
        
