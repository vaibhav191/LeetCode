class Node():
    def __init__(self):
        self.end = False
        self.next = [None]*26
class Trie:
    def __init__(self):
        self.start = Node()
        self.ord_ = lambda c: ord(c) - ord('a')
        
    def insert(self, word: str) -> None:
        head = self.start
        for c in word:
            if not head.next[self.ord_(c)] :
                head.next[self.ord_(c)] = Node()
            head = head.next[self.ord_(c)]
        head.end = True

    def search(self, word: str) -> bool:
        head = self.start
        for c in word:
            if not head.next[self.ord_(c)]:
                return False
            head = head.next[self.ord_(c)]
        return head.end

    def startsWith(self, prefix: str) -> bool:
        head = self.start
        for c in prefix:
            if not head.next[self.ord_(c)]:
                return False
            head = head.next[self.ord_(c)]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
