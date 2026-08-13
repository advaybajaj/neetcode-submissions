# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
    
        def dfs(node, low, high) -> bool:

            if not node:
                return True

            if low >= node.val or node.val >= high:
                return False

            return dfs(node.left, low, min(node.val, high)) and dfs(node.right, max(node.val, low), high)

        return dfs(root, -float("inf"), float("inf"))