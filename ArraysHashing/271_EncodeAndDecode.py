class Solution:

    def encode(self, strs: List[str]) -> str:
        new_s = ""
        for s in strs:
            new_s+= str(len(s))+"#"+s
        return new_s
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j]!= '#':
                j+=1
            length=int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j+1+length
        
        return res
            
        
