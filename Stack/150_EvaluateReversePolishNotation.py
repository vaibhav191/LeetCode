class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        from collections import deque
        deck = []
        operation = {
            '+' : lambda x,y: x + y,
            '-' : lambda x,y: x-y,
            '*' : lambda x,y: x*y,
            '/': lambda x,y: int(x/y)
        }
        for token in tokens:
            if token in operation:
                y = deck.pop()
                x = deck.pop()
                deck.append(operation[token](x,y))
            else:
                deck.append(int(token))
            # print(token, deck)
        return deck.pop()
