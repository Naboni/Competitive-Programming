# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder: return
        if len(preorder) == 1: return TreeNode(postorder.pop())
        node = TreeNode(postorder.pop())
        mid = preorder.index(postorder[-1])
        node.right = self.constructFromPrePost(preorder[mid:], postorder)
        node.left = self.constructFromPrePost(preorder[1:mid], postorder)
        return node