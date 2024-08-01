# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self, node, paths, curr):
        if node is None:
            return
        
        curr.append(node.val)
        
        if node.left is None and node.right is None:
            paths.append(curr[:])
            
        if node.left:
            self.dfs(node.left, paths, curr)
            
        if node.right:
            self.dfs(node.right, paths, curr)
            
        curr.pop()
        
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        paths = []
        curr = []
        ans = []
        
        self.dfs(root, paths, curr)
        
        for path in paths:
            if sum(path) == targetSum:
                ans.append(path)
                
                
        return ans