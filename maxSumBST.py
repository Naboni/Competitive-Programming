# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def postorder(root):
            if not root:
                return True, 0, -inf, inf
            leftValid, leftSumm, leftMax, leftMin = postorder(root.left)
            rightValid, rightSumm, rightMax, rightMin = postorder(root.right)

            if leftValid and rightValid and leftMax < root.val < rightMin:
                currSumm = leftSumm + rightSumm + root.val
                currMax = rightMax if rightMax != -inf else root.val
                currMin = leftMin if leftMin != inf else root.val
                self.res = max(self.res, currSumm)
                return True, currSumm, currMax, currMin
            return False, None, None, None
        postorder(root)
        return self.res