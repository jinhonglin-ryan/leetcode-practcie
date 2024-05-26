# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.count = 0
        
    def helper(self, node, max_val):
        if node is None:
            return
        
        if node.val >= max_val:
            self.count += 1
            max_val = node.val
        
        self.helper(node.left, max_val)
        self.helper(node.right, max_val)
        
        
        
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root is None:
            return 0
        self.helper(root, root.val)
        return self.count 
        
        
        