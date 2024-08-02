# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        if root is None:
            return 0
        
        left = root.left
        right = root.right
        
        lh = 1
        rh = 1
        
        while left:
            left = left.left
            lh += 1
            
        while right:
            right = right.right
            rh += 1
            
        if rh == lh:
            return (2 ** lh) - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)