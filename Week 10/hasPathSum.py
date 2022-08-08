class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, summ):
            if not root:
                return False
            if not root.left and not root.right and summ+root.val == targetSum:
                return True
            return dfs(root.left, summ+root.val) or dfs(root.right, summ+root.val)
        return dfs(root, 0)
