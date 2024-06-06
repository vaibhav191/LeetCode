class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        count_cards = Counter(hand)
        #O(n) algorithm
        for card in hand:
            start_card = card
            # Find the start of the potential straight sequence
            while count_cards[start_card - 1]:
                start_card -= 1

            # Process the sequence starting from start_card
            while start_card <= card:
                while count_cards[start_card]:
                    # Check if we can form a consecutive sequence
                    # of groupSize cards
                    for i in range(start_card, start_card + groupSize):
                        if not count_cards[i]:
                            #print(start_card, i, count_cards)
                            return False
                        count_cards[i] -= 1
                start_card += 1
        return True
