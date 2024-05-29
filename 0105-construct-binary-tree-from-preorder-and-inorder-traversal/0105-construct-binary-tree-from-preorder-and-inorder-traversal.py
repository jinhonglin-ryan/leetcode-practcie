# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def build(self, preorder, inorder, pl, pr, il, ir): 
        if pl > pr or il > ir:
            return None
        
        root_val = preorder[pl]
        k = inorder.index(root_val)
        root = ListNode(val=root_val)
        
        root.left = self.build(preorder, inorder, pl + 1, pl + 1 + k - 1 - il, il, k - 1)
        root.right = self.build(preorder, inorder, pl + 1 + k - 1 - il + 1, pr, k + 1, ir)
        
        return root
        
        
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        return self.build(preorder,inorder, 0, len(preorder) - 1, 0, len(inorder) - 1)
        
    