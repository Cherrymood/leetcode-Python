class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:
            return

        if val == root.val:
            return root

        if val < root.val:
            if root.left:
                return self.searchBST(root.left, val)
        if val > root.val:
            if root.right:
                return self.searchBST(root.right, val)