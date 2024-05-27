# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    # 两棵树相等的条件：
    # 1. 根结点相等
    # 2. 并且 左子树等于左子树
    # 3. 并且 右子树等于右子树
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        
        if (p is None and q is not None) or (p is not None and q is None):
            return False
        
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    
    # subRoot是root子树的条件：
    # 1. subRoot 和 root 两棵树完全一样
    # 2. 或者 subRoot 和 root的左子树一样
    # 3. 或者 subRoot 和 root的右子树一样 
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        
        if root is None and subRoot is None:
            return True
        
        if root is None or subRoot is None:
            return False
        
        return self.isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        