class Node():
    def __init__(self, letter):
        self.val = letter
        self.next = {}
class Trie:
    def __init__(self):
        self.start = Node("")

    def insert(self, word: str) -> None:
        head = self.start
        for c in word:
            if c not in head.next:
                head.next[c] = Node(c)
            head = head.next[c]
        head.next['X'] = None
    def search(self, word: str) -> bool:
        head = self.start
        for c in word:
            if c not in head.next:
                return False
            head = head.next[c]
        if 'X' in head.next:
            return True
    def startsWith(self, prefix: str) -> bool:
        head = self.start
        for c in prefix:
            if c not in head.next:
                return False
            head = head.next[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
