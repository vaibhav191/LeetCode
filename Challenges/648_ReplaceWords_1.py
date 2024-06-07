#O(n*m)
#O(d*w + s*w)
#(d = number of words in dic, s = number of words in sentence, w = avg length of words )
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dicSet = set(dictionary)
        # print(dicSet)
        sentence = sentence.split(" ")
        newS = []
        for word in sentence:
            found = False
            for i in range(len(word)):
                if word[:i] in dicSet:
                    # print(word, word[:i])
                    newS.append(word[:i])
                    found = True
                    break
            if not found:
                newS.append(word)
        return " ".join(newS)
