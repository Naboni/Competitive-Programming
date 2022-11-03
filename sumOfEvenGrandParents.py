# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(node, par, gp):
            if not node:
                return 0
            left, right = dfs(node.left, node.val, par), dfs(node.right, node.val, par) 
            if gp and gp % 2 == 0:
                return node.val + left + right
            return left + right
        return dfs(root, None, None)