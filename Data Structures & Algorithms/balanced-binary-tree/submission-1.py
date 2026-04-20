# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return True

            leftD = dfs(root.left)
            rightD = dfs(root.right)

            if leftD < 0:
                return -1
            if rightD < 0:
                return -1

            if abs(rightD - leftD) > 1:
                return -1

            return 1 + max(leftD, rightD)
            
        return dfs(root)>=0








        