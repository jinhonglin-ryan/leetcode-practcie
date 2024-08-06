# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.max_len = 0
        
    def dfs(self, node, direc, curr_depth):
        if node is None:
            return
        
        self.max_len = max(self.max_len, curr_depth)
        
        if direc == 'left':
            self.dfs(node.left, 'left', 1)
            self.dfs(node.right, 'right', curr_depth + 1)
            
        if direc == 'right':
            self.dfs(node.right, 'right', 1)
            self.dfs(node.left, 'left', curr_depth + 1)
    
        
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.dfs(root.left, 'left', 1)
        self.dfs(root.right, 'right', 1)
        
        return self.max_len