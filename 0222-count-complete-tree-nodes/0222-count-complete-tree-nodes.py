# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.cnt = 0
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else :
            self.cnt += 1
            
        if root.left:
            self.countNodes(root.left)
        
        if root.right:
            self.countNodes(root.right)
            
        return self.cnt 
        
        