# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # dfs
        # def dfs(node):
        #     if not node:
        #         return 0
        #     if node.left and not node.left.left and not node.left.right:
        #         return node.left.val + dfs(node.right)
        #     return dfs(node.left) + dfs(node.right)
        # return dfs(root)
        # bfs
        q = deque([root])
        res = 0
        while q:
            node = q.popleft()
            if node.left and not node.left.left and not node.left.right:
                res += node.left.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return res