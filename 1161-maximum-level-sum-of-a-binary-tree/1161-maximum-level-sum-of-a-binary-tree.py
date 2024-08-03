# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return
        
        queue = deque([root])
        ans = []
        while queue:
            n = len(queue)
            level = []
            for _ in range(n):
                node = queue.popleft()
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
                    
            if level:
                ans.append(level)
        
        max_level = 1
        max_sum = sum(ans[0])
        curr_level = 1
        
        for level in ans:
            curr_sum = sum(level)
            if curr_sum > max_sum:
                max_sum = curr_sum
                max_level = curr_level
            curr_level += 1
        
        return max_level 
            