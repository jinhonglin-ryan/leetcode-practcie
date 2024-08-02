# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMin(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        
        if root is None:
            return None
        
        if root.val == key:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            # Node with two children: Get the inorder successor (smallest in the right subtree)
            temp = self.findMin(root.right)
            
            # Copy the inorder successor's content to this node
            root.val = temp.val
            
            # Delete the inorder successor
            root.right = self.deleteNode(root.right, temp.val)
            
            
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
            
        else: 
            root.right = self.deleteNode(root.right, key)
            
        return root 