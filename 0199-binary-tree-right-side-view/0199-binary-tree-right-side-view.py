# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def height(self, root):
        if root is None:
            return 0
        
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        return max(left_height, right_height) + 1
    
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        h = self.height(root)
        ans = []
        queue = [root]
        
        while h > 0:
            n = len(queue)
            right_most_node = queue[n - 1]
            ans.append(right_most_node.val)
        
            
            for _ in range(n):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)    
            h -= 1 
        
        return ans
        
        