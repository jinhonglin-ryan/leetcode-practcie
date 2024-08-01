# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.inorder = []
        
    def dfs(self, node):
        if node is None:
            return
        
        self.dfs(node.left)
        self.inorder.append(node.val)
        self.dfs(node.right)
        
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.dfs(root)
        cnt = defaultdict(int)
        for num in self.inorder:
            cnt[num] += 1
        
        max_keys = []
        max_value = float('-inf')
    
        for key, value in cnt.items():
            if value > max_value:
                max_value = value
                max_keys = [key]
            elif value == max_value:
                max_keys.append(key)

        return max_keys 