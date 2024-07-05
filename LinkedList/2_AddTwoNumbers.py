# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ans = ListNode(0, None)
        carry = 0
        while l1 or l2:
            if l1:
                dummy.val += l1.val
                l1 = l1.next
            if l2:
                dummy.val += l2.val
                l2 = l2.next
            carry = dummy.val // 10
            dummy.val = dummy.val % 10
            if l1 or l2 or carry:
                dummy.next = ListNode(carry, None)
            dummy = dummy.next
        return ans

