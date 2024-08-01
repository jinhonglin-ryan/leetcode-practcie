# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def dfs(self, node, leaves):
        if node is None:
            return
        
        if node.left is None and node.right is None:
            leaves.append(node.val)
            
        if node.left:
            self.dfs(node.left, leaves)
            
        if node.right:
            self.dfs(node.right, leaves)

        
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        a = []
        b = []
        self.dfs(root1, a)
        self.dfs(root2, b)
        
        return a == b
        