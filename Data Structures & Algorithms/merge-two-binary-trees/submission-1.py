# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1

        def dfs(s, t):
            if not s and not t:
                return None

            val = (s.val if s else 0) + (t.val if t else 0)
            node = TreeNode(val)

            node.left = dfs(s.left if s else None, t.left if t else None)
            node.right = dfs(s.right if s else None, t.right if t else None)

            return node

        return dfs(root1, root2)