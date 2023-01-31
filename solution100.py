
class TreeNode:
def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True
        if not p or not q:
            return False

        stackp = [p]
        stackq = [q]

        while stackp and stackq:
            node1 = stackp.pop()
            node2 = stackq.pop()
            if node1.val != node2.val:
                return False

            if node1.left and node2.left:
                stackp.append(node1.left)
                stackq.append(node2.left)
            elif node1.left or node2.left:
                return False

            if node1.right and node2.right:
                stackp.append(node1.right)
                stackq.append(node2.right)
            elif node1.right or node2.right:
                return False

        return True


