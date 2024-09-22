class Node:
    def __init__(self, end = False, children = None, value = None):
        self.end = end
        self.children = children if children is not None else {}
        self.value = value
    def __str__(self):
        return f"Node: (value={self.value}, end={self.end}, children={self.children})"

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        nums = [i for i in range(1, n+1)]
        print(nums)
        head = Node()
        for num in nums:
            ptr = head
            for c in str(num):
                # print(num, c)
                if c not in ptr.children:
                    ptr.children[c] = Node(value = c)
                # print(ptr)
                ptr = ptr.children[c]
            ptr.end = True
        
        nums = []

        def dfs(ptr, s):
            if ptr.end == True:
                nums.append(int(s))

            for i in range(10):
                if str(i) in ptr.children:
                    dfs(ptr.children[str(i)], s + str(i))
        
        dfs(head, "")

        return nums
