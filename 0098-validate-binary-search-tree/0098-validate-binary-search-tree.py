# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def inorder_traversal(self, root):
        ans = []
        
        def inorder(node):
            
            if node is None:
                return
            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)
            
        inorder(root)
        return ans 
    
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        # 思路：inorder traversal
        # 然后查看返回的是否是升序数组
        inorder_list = self.inorder_traversal(root)
        
        # 检查列表是否为严格升序
        for i in range(1, len(inorder_list)):
            if inorder_list[i-1] >= inorder_list[i]:
                return False
        return True