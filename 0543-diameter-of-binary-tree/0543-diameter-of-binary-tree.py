# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    # 有两种情况：
    # 1. 二叉树的直径=左子树高度+右子树高度。（其直径长度所对应的路径是穿过根节点的）
    # 2. 二叉树的直径=所有子树中最大直径长度。（其直径长度所对应的路径是没有穿过根节点的）
    # 所以：二叉树的直径=max(左子树高度+右子树高度,所有子树中最大直径长度)。
    
    def __init__(self):
        self.ans = 0
    
    def dfs(self, node):
        if node is None:
            return 0
        
        left_height = self.dfs(node.left)
        right_height = self.dfs(node.right)
        self.ans = max(self.ans, left_height + right_height)
        
        return max(left_height, right_height) + 1 
    
    
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root)
        return self.ans