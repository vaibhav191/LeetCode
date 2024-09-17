class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split(" ")
        s2 = s2.split(" ")
        s1 = s1+s2
        count = Counter(s1)
        res = []
        for k,v in count.items():
            if v == 1:
                res.append(k)
        return res
