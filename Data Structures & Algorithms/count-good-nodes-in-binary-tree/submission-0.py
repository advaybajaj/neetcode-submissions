# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 1
        
        def dfs(node, threshold):
            nonlocal count

            if node.val >= threshold:
                count += 1
                threshold = node.val
            
            if node.left:
                dfs(node.left, threshold)
            if node.right:
                dfs(node.right, threshold)

        if root.left:
            dfs(root.left, root.val)
        if root.right:
            dfs(root.right, root.val)
        
        return count