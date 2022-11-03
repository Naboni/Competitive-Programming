# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def backtrack(node, path):
            if not node:
                return
            if not node.left and not node.right:
                res.append(path + [str(node.val)])
                return
            backtrack(node.left, path+[str(node.val)])
            backtrack(node.right, path+[str(node.val)])
        backtrack(root, [])
        return ["->".join(a) for a in res]
