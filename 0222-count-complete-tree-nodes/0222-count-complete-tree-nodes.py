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
        
        left = root
        right = root
        
        left_height = 0
        right_height = 0
        
        while left:
            left = left.left
            left_height += 1
            
        while right:
            right = right.right
            right_height += 1
            
        if left_height == right_height:
            return (2 ** left_height) - 1
        
        leftNum = self.countNodes(root.left)
        rightNum = self.countNodes(root.right)
        
        return leftNum + rightNum + 1