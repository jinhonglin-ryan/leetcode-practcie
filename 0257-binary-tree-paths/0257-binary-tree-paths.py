# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def dfs(self, node, path, ans):
        if node is None:
            return
        
        # 将当前node的值转换为字符串并加入path
        path.append(str(node.val))
        
        # 如果当前node是叶子节点，将path加入ans
        if node.left is None and node.right is None:
            ans.append("->".join(path))
        
        # 如果当前node不是叶子节点，开始递归
        if node.left:
            self.dfs(node.left, path, ans)
        
        if node.right:
            self.dfs(node.right, path, ans)
        
        # 回溯，移除当前节点
        path.pop()
        
        
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        path = []
        ans = []
        self.dfs(root, path, ans)
        return ans