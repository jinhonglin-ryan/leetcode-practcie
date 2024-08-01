# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
        
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 必须要找到leaf node，所以需要考虑当前节点是不是leaf node
        # 当前节点是leaf node: 那就返回1
        # 当前节点不是leaf node: 要去左右子树递归找leaf node
        
        if root is None:
            return 0
        
        # 当前节点是leaf node
        if root.left is None and root.right is None:
            return 1
        
        # 当前节点不是leaf node
        # 1. 如果左右子树都有的话，当前深度就是左右子树的最小深度+1
        if root.left and root.right:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        # 2. 如果只有左子树 没有 右子树，需要去左子树找leaf node
        if root.left and root.right is None:
            return 1 + self.minDepth(root.left)
        
        # 3. 如果只有右子树 没有 左子树，需要去右子树找leaf node
        return 1 + self.minDepth(root.right)
        
        