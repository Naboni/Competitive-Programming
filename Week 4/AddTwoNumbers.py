# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cr,sm=0,0
        r=ans=ListNode()
        while l1 or l2 or cr:
            d1,d2=0,0
            if l1:
                d1=l1.val
            if l2:
                d2=l2.val
            sm=d1+d2+cr
            cr=sm//10
            r.next=ListNode(sm%10)
            r=r.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return ans.next
