# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.ans = 0
        self.maxDepth = 0
    
    def dfs(self, node, depth):
        if node is None:
            return
        
        if node.left is None and node.right is None:
            if depth > self.maxDepth:
                self.maxDepth = depth
                self.ans = node.val
                
        self.dfs(node.left, depth + 1)
        self.dfs(node.right, depth + 1)
        
                
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root, 1)
        return self.ans
        