class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charsmap = [0]*26
        for ch in chars:
            pos = ord(ch) - ord('a')
            charsmap[pos] += 1
        goodStrings = 0
        for w in words:
            log = [0]*26
            possible = True
            for c in w:
                pos = ord(c) - ord('a')
                log[pos] += 1
                if log[pos]>charsmap[pos]:
                    possible = False
                    break
            if possible:
                goodStrings += len(w)
        return goodStrings
