# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        output, stack = [], []
        i = 0
        while head:
            output.append(0)
            val = head.val
            while len(stack) > 0 and stack[-1][1] < val:
                output[stack.pop()[0]] = val
            stack.append((i, val))
            head = head.next
            i += 1

        return output
