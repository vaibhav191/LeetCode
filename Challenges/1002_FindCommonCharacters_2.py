class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        if len(words) == 1:
            return list(words[0])
        word = set(words[0])
        for i in word:
            ans = min([w.count(i) for w in words])
            #print(ans)
            res += i*ans
        return res
            

