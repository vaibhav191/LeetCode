class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        #greedy algorithm
        #pick the next smallest value and check for consequtive pairs with it, if not available return false
        card_count = Counter(hand)
        min_heap = list(card_count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            cur_card = min_heap[0]
            for i in range(groupSize):
                if card_count[cur_card+i]==0:
                    return False
                card_count[cur_card+i] -= 1
                if card_count[cur_card+i] == 0:
                    if cur_card+i != heapq.heappop(min_heap): # when popping, we are checking if the element being popped, was it the next smallest available element? if not, that means the sequence broke and we need not check other possiblities
                        #The condition "if currentCard + i not in hash map" enhances the solution's efficiency. It allows the function to terminate early when a required card for forming a group is absent. This prevents unnecessary decrement operations and subsequent checks, thus optimizing the overall performance to some extent.
                        return False
        return True
