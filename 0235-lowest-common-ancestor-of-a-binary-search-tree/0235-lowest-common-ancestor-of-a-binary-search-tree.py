# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
#         # Method 1: Recursion
#         if root is None or root == p or root == q:
#             return root
    
#         # 递归在左子树搜索p or q
#         left = self.lowestCommonAncestor(root.left, p, q) if root.left else None
#         # 递归在右子树搜索p or q
#         right = self.lowestCommonAncestor(root.right, p, q) if root.right else None

#         # 如果在左右子树中都找到了目标节点，则当前root是LCA
#         if left and right:
#             return root

#         # 如果只在左子树找到，则返回左子树的结果
#         if left:
#             return left

#         # 如果只在右子树找到，则返回右子树的结果
#         if right:
#             return right

#         # 如果两边都没有，则返回None
#         return None

        # Method 2: Iterative
        lca = root
        
        while lca:
            if lca.val > p.val and lca.val > q.val:
                lca = lca.left
            elif lca.val < p.val and lca.val < q.val:
                lca = lca.right
            else:
                break
        return lca
        
