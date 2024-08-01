# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.inorder_list = []
        
    def dfs(self, node):
        if node is None:
            return
        
        self.dfs(node.left)
        self.inorder_list.append(node.val)
        self.dfs(node.right)
        
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 中序遍历
        # 获得升序数组
        # 找到相邻的最小差值即可
        self.dfs(root)
        min_diff = float('inf')
        for i in range(1, len(self.inorder_list)):
            if self.inorder_list[i] - self.inorder_list[i - 1] < min_diff:
                min_diff = self.inorder_list[i] - self.inorder_list[i - 1]
                
        return min_diff 
            
        
        