# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
		newNode=head
		output = newNode
		array = []
		while head != None:
			array.append(head.val)
			head=head.next
		array.sort()
		for num in array:
			newNode.val = num
			newNode = newNode.next
		return output
