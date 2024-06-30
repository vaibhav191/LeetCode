class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        from collections import deque
        deck = deque()
        res = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(deck))
                return
            if openN < n:
                deck.append("(")
                backtrack(openN + 1, closeN)
                deck.pop()
            if closeN < openN:
                deck.append(")")
                backtrack(openN, closeN + 1)
                deck.pop()
        backtrack(0,0)
        return res
