# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        cur = head
        future = head
        for _ in range(n):
            future = future.next
        while future:
            prev = cur
            cur = cur.next
            future = future.next
        
        if prev:
            prev.next = cur.next
        else:
            head = cur.next
        return head
