class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = [None]*26
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = TrieNode()
        for word in dictionary:
            ptr = trie
            for char in word:
                if ptr.children[ord(char) - ord('a')] is None:
                    ptr.children[ord(char) - ord('a')] = TrieNode()
                ptr = ptr.children[ord(char) - ord('a')]
            ptr.isEnd = True
        sentence = sentence.split(" ")
        newS = []
        print(trie.children)
        for word in sentence:
            ptr = trie
            if ptr.children[ ord(word[0]) - ord('a')] is None:
                print(ord(word[0]) - ord('a'))
                newS.append(word)
                continue
            notMatching = False
            isEnd = False
            wordEnd = False
            for i,ch in enumerate(word):
                if ptr.children[ord(word[i]) - ord('a')] is None:
                    notMatching = True
                    break
                ptr = ptr.children[ord(word[i]) - ord('a')]
                if ptr.isEnd:
                    isEnd = True
                    break
                if i == len(word)-1:
                    wordEnd=True
                    break
            if notMatching:
                newS.append(word)
                continue
            if wordEnd:
                newS.append(word)
                continue
            if isEnd:
                newS.append(word[:i+1])
                continue
        print(newS)
        return " ".join(newS)
