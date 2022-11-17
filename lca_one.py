# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.dfs(root, set([p, q]))[1]

    def dfs(self,root,nodes):
        if not root:
            return False, None
        left = self.dfs(root.left, nodes)
        right = self.dfs(root.right, nodes)
        if root in nodes or (left[0] and right[0]):
            return True, root
        elif left[0] or right[0]:
            return True, left[1] or right[1]
        return False, None