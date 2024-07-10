class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        deck = deque(range(1, n+1))
        kick = 0
        while len(deck) > 1:
            kick += (k-1)
            kick%=len(deck)
            # print(deck, kick, deck[kick])
            del(deck[kick])
        return deck[0]

