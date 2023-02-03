# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        column = defaultdict(list)
        def dfs(root, col, row):
            if not root:
                return
            column[col].append((row, root.val))
            dfs(root.left, col-1, row+1)
            dfs(root.right, col+1, row+1)
        dfs(root, 0, 0)
        res = []
        for c in sorted(column.keys()):
            temp = []
            for n in sorted(column[c]):
                temp.append(n[1])
            res.append(temp)
        return res