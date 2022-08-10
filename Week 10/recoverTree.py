# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack, recovered = [], []
        prev = TreeNode(float('-inf'))
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            node = stack.pop()
            if node.val < prev.val:
                recovered.append((prev, node))
            prev, curr = node, node.right
        recovered[0][0].val, recovered[-1][1].val = recovered[-1][1].val, recovered[0][0].
