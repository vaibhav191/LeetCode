# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next:
            return head
        #find midpoint
        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None

        #reverse from midpoint
        cur = slow
        prev = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        first, second = head, prev
        
        def recur(l1, l2):
            if not l1:
                return l2
            if not l2:
                return l1
            nxt = l1.next
            l1.next = l2
            l1 = nxt
            return recur(l2, l1)
        recur(first, second)
        
