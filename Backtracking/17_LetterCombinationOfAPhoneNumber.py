# O(4^N) |  N = len-digits
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k","l"],
            6:["m","n","o"],
            7:["p","q","r","s"],
            8:["v","t","u"],
            9:["y","w","x","z"],
        }
        ans = []
        def backtrack(i, subset):
            if len(digits) == 0:
                return
            if i == len(digits):
                ans.append("".join(subset))
                return
            for c in mapping[int(digits[i])]:
                subset.append(c)
                backtrack(i+1, subset)
                subset.pop()
        backtrack(0, [])
        return ans
            
        
