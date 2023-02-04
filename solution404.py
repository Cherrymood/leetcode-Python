# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def accumulate_left_leaves(self, root: Optional[TreeNode], is_left: bool) -> list[int]:
        if not root:
            return 0

        is_leaf: bool = False
        if not root.left and not root.right:
            is_leaf = True

        if is_leaf and is_left:
            return root.val
        elif is_leaf and not is_left:
            return 0

        return self.accumulate_left_leaves(root.left, True) + self.accumulate_left_leaves(root.right, False)


    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        result: list[int] = []
        result.append(self.accumulate_left_leaves(root, False))
        return sum(result)
Console
