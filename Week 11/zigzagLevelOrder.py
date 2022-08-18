# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root] if root else [])
        res = []
        flag = True
        while q:
            row = []
            for _ in range(len(q)):
                node = q.popleft()
                row.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(row) if flag else res.append(row[::-1])
            flag = not flag
        return res
