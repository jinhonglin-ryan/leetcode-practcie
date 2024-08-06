# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.max_length = 0
        
    def dfs(self, node, direc, length):
        if node is None:
            return
        
        # Update the maximum length
        self.max_length = max(self.max_length, length)
        
        # If direction is 0, we are going left, so next we go right
        if direc == 0:
            if node.left:
                self.dfs(node.left, 1, length + 1)  # Change direction to right
            if node.right:
                self.dfs(node.right, 0, 1)  # Reset length when changing direction
        else:
            # If direction is 1, we are going right, so next we go left
            if node.right:
                self.dfs(node.right, 0, length + 1)  # Change direction to left
            if node.left:
                self.dfs(node.left, 1, 1)  # Reset length when changing direction

    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        
        self.dfs(root, 0, 0)
        self.dfs(root, 1, 0)
        
        return self.max_length