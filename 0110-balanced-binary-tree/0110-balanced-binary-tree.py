# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.balanced = True 
        
        
    def isBalanced(self, root):
        # dfs 
        def dfs(node):
            if node is None:
                # node is None <=> height is 0
                return 0
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            if abs(left_height - right_height) > 1:
                self.balanced = False
                
            return 1 + max(left_height, right_height)
        
        
        dfs(root)
        return self.balanced