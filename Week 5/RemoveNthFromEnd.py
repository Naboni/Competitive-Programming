# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counter = 0
        current = head
        while current.next is not None:
            counter += 1
            current = current.next
        counter += 1
        
        current = head
        for i in range(counter - n - 1):
            current = current.next
        
        if counter == n:
            head = head.next
        else:
            current.next = current.next.next
        
        return head
