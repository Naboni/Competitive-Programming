# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)>2: 
            return self.mergeTwoLists(self.mergeKLists(lists[:len(lists)//2]),self.mergeKLists(lists[len(lists)//2:]))
        elif len(lists)==1: 
            return lists[0]
        elif len(lists)==0: 
            return None
        else: 
            return self.mergeTwoLists(lists[0], lists[1])
        
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = iterator = ListNode()
        while l1 or l2:
            v1 = l1.val if l1 else float("inf")
            v2 = l2.val if l2 else float("inf")
            if v1<=v2:
                iterator.next = l1
                l1 = l1.next
            else:
                iterator.next = l2
                l2 = l2.next
            iterator = iterator.next
        return head.next
