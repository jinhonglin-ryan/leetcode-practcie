# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self, node, max_val):
        if node is None:
            return 0
        
        count = 0
        if node.val >= max_val:
            count += 1
            max_val = node.val
        
        count += self.dfs(node.left, max_val) + self.dfs(node.right, max_val)
        return count
        
        
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root, root.val)
        
    # dfs: 从根节点出发，遍历完所有的节点，能找到好节点的数量
    # dfs(None, max_val) = 0
    # dfs(u, max_val) = 本身是否是一个好节点 + dfs(u.left, max_val) + dfs(u.right, max_val)
        