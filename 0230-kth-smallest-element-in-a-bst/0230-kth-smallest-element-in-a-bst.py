# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def in_order_traversal(self, root):
        ans = []
        def inorder(node):
            if node is None:
                return 
            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)
        inorder(root)
        return ans
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        inorder_list = self.in_order_traversal(root)
        sorted_inorder_list = sorted(inorder_list)
        return sorted_inorder_list[k - 1]
        