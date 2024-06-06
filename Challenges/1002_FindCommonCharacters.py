class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counter = []
        for word in words:
            count = [0]*26
            for ch in word:
                count[ord(ch)- ord('a')] += 1
            counter.append(count)
        min_counter = [101]*26
        ans = []
        for i in range(26):
            for j in range(len(counter)):
                min_counter[i] = min(min_counter[i],counter[j][i])
            if min_counter[i]!= 101:
                for ch in range(min_counter[i]):
                    ans.append(chr(ord('a')+i))
        print(min_counter)
        return ans
