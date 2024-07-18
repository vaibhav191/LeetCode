class TrieNode():
    def __init__(self):
        self.children = {}
        self.end = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        ptr = self.root
        for c in word:
            if c not in ptr.children:
                ptr.children[c] = TrieNode()
            ptr = ptr.children[c]
        ptr.end = True

    def search(self, word: str) -> bool:
        def dfs(j, ptr):
            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for child in ptr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in ptr.children:
                        return False
                    ptr = ptr.children[c]
            return ptr.end
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
