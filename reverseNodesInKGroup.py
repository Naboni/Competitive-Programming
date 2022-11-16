# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:   
        # check if it needs to be reversed
        curr = head
        for _ in range(k):
            if not curr:
                return head
            curr = curr.next
        # standard reversing
        prev, curr = None, head 
        for _ in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # after reverse head is now tail of the group
        head.next = self.reverseKGroup(curr, k)
        return prev