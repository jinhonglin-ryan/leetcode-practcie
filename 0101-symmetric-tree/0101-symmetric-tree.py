# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def dfs(self, a, b):
        if a is None and b is None:
            return True
        
        if a is None or b is None or a.val != b.val:
            return False
        
        return self.dfs(a.left, b.right) and self.dfs(a.right, b.left)
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        return self.dfs(root.left, root.right)
        