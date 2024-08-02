# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.cnt = 0
        
    def dfs(self, root):
        if root is None:
            return
        
        if root.left:
            if root.left.left is None and root.left.right is None:
                self.cnt += root.left.val
                
        self.dfs(root.left)
        self.dfs(root.right)
        
        
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root)
        return self.cnt
    