class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return

        queue: list = [root]
        result: list = []

        while queue:
            next_queue: list = []
            level: list = []

            for root in queue:
                level.append(root.val)
                if root.left:
                    next_queue.append(root.left)
                if root.right:
                    next_queue.append(root.right)
            result.append(level)
            queue = next_queue

        return result

