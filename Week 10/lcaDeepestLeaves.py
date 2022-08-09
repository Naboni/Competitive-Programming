# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if not root: 
                return 0, None
            heightLeft,  lcaLeft  = dfs(root.left)
            heightRight, lcaRight = dfs(root.right)
            
            if heightLeft > heightRight: 
                return heightLeft + 1, lcaLeft
            elif heightLeft < heightRight: 
                return heightRight + 1, lcaRight
            else:
                return heightLeft + 1, root

        return dfs(root)[1]
