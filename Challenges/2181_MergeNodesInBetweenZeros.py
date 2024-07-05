# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head
        while head.next.next is not None:
            if head.next.val == 0:
                head = head.next
            else:
                head.val += head.next.val
                head.next = head.next.next
        head.next = None
        return start
