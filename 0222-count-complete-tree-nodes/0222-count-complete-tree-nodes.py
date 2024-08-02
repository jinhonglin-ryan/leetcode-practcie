# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 终止条件1：如果当前节点是空节点，返回0
        if root is None:
            return 0
        
        # 终止条件2：如果当前节点的左子树和右子树是一个满二叉树，可以利用公式把当前节点+左子树和右子树的所有node count算出来
        # 如果当前节点的左子树和右子树是一个满二叉树，则满足当前节点一直往左走的深度 和当前节点一直往右走的深度一样 
        left = root.left
        right = root.right
        
        left_height = 1
        right_height = 1
        
        while left:
            left = left.left
            left_height += 1
            
        while right:
            right = right.right
            right_height += 1
            
        if left_height == right_height:
            return (2 ** left_height) - 1
        
        # 单层递归，如果当前节点的左右子树不是满二叉树，则递归去算左子树的node count 和右子树的node count，然后加上当前节点+1返回 
        leftNum = self.countNodes(root.left)
        rightNum = self.countNodes(root.right)
        
        return leftNum + rightNum + 1