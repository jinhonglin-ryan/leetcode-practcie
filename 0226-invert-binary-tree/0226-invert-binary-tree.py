# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        # recursion 
        
        if not root:
            return None
        
        # 可以先交换左右子树，再分别翻转左右子树
        temp = root.left
        root.left = root.right
        root.right = temp
        
        
       
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root 
    
    
        # 或者先翻转左右子树，再交换左右子树
        # left = self.invertTree(root.left)
        # right = self.invertTree(root.right)
        # root.right = left 
        # root.left = right
        # return root 
        
        
        