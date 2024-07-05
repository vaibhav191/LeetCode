# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if head.next.next is None:
            return [-1, -1]
        crits_index = []
        prev = head
        cur = head.next
        nxt = cur.next
        i = 1
        while nxt:
            if (prev.val<cur.val and nxt.val < cur.val) or (prev.val>cur.val and nxt.val>cur.val):
                crits_index.append(i)
            i += 1
            prev,cur,nxt = prev.next, cur.next, nxt.next
        if len(crits_index) < 2:
            return [-1, -1]
        min_dist = float('inf')
        max_dist = crits_index[-1] - crits_index[0]
        for i in range(len(crits_index) - 1):
            min_dist = min(min_dist, crits_index[i+1] - crits_index[i])
        return [min_dist, max_dist]
