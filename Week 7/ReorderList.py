# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        half = slow.next
        slow.next = None
        prev = None
        
        while half:
            temp = half.next
            half.next = prev 
            prev = half
            half = temp
        
        first, second = head, prev
        
        while second:
            temp1, temp2 = first.next, second.next
            
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
