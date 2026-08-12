# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        flag = True

        def height(node):
            nonlocal flag

            if not node:
                return 0

            l = height(node.left)
            r = height(node.right)

            if abs(l - r) > 1:
                flag = False

            return 1 + max(l, r)
            
        height(root)
        return flag
