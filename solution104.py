# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root:
            if (not root.left and not root.right):
                return 1
            left = right = 0
            if (root.left):
                left = self.maxDepth(root.left)
            if (root.right):
                right = self.maxDepth(root.right)

            return 1 + max(left, right)

        return 0
