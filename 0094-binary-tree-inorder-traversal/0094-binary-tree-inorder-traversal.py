# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self, node, x):
        if node is None:
            return
        
        self.dfs(node.left, x)
        x.append(node.val)
        self.dfs(node.right, x)
        
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        a = []
        self.dfs(root, a)
        return a 
        