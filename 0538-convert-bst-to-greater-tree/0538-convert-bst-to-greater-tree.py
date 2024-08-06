# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.pre = 0
        
    def dfs(self, node):
        if node is None:
            return
        
        self.dfs(node.right)
        x = node.val
        node.val += self.pre
        self.pre += x
        self.dfs(node.left)    
        
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.dfs(root)
        return root