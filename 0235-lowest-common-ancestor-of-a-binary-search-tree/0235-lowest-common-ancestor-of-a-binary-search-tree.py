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
        
        lca = root
        
        while True:            
            if lca.val > p.val and lca.val > q.val:
                lca = lca.left
                
            elif lca.val < p.val and lca.val < q.val:
                lca = lca.right
                
            else:
                break
                
        return lca
            