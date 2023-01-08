# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        result = 0  # For summation of the left leaves values

        stack = [(root, False)]  # Using stack with tuple (Node, Boolean Value)

        # If the stack is not empty
        while stack:

            # Get the topmost element from the stack (LIFO)
            currentNode, isLeft = stack.pop()

            if not currentNode:  # If there's no node
                continue

            if not currentNode.left and not currentNode.right:  # If the current Node is a leaf i.e. current Node's left and right childs are null.
                if isLeft:  # If the current Node is leaf then check if it's a left leaf or not since we only want left leaf and not the right left.
                    result += currentNode.val  # If it's a left leaft then add it to the result

                # Otherwise we're yet to reach the leaf node so go ahead and the left and right child of the current node in the stack.
            else:
                stack.append((currentNode.left, True))  # If we encountered a left leaf node then mark it as True
                stack.append((currentNode.right, False))

        return result