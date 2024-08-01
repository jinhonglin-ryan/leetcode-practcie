# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.cnt = 0
        
    def dfs(self, node):
        if node is None:
            return
        
        if node.left:
            if node.left.left is None and node.left.right is None:
                self.cnt += node.left.val
                
        self.dfs(node.left)
        self.dfs(node.right)
        
        
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root)
        return self.cnt
        