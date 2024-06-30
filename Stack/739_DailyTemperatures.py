class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        from collections import deque
        deck = deque()
        
        for i,temp in enumerate(temperatures):
            if not deck:
                deck.append(i)
                continue
            while deck and temp > temperatures[deck[-1]]:
                pos = deck.pop()
                temperatures[pos] = i - pos
            deck.append(i)

        while deck:
            temperatures[deck.pop()] = 0

        return temperatures
