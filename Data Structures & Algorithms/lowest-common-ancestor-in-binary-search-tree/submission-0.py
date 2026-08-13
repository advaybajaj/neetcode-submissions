# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lower = p if p.val < q.val else q
        higher = p if p.val > q.val else q

        if root.val == lower.val or root.val == higher.val:
            return root

        if lower.val < root.val and higher.val > root.val:
            return root
        elif lower.val < root.val and higher.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif lower.val > root.val and higher.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        