# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.ans = 0

    def dfs(self, node):
        if not node:
            return 0
        left_height = self.dfs(node.left)                     # 左子树高度
        right_height = self.dfs(node.right)                   # 右子树高度
        self.ans = max(self.ans, left_height + right_height)  # 维护所有路径中的最大直径
        return max(left_height, right_height) + 1             # 返回该节点的高度 = 左右子树最大高度 + 1

    
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.dfs(root)
        return self.ans
    