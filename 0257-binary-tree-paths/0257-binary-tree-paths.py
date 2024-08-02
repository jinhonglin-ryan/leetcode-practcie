# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self, node, curr, paths):
        if node is None:
            return
        
        curr.append(str(node.val))
        
        if node.left is None and node.right is None:
            paths.append("->".join(curr))
            
        self.dfs(node.left, curr, paths)
        self.dfs(node.right, curr, paths)
        
        curr.pop()
        
        
        
        
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        
        paths = []
        curr = []
        self.dfs(root, curr, paths)
        
        return paths
        