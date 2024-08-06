# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.cnt = 0
        self.map = defaultdict(int)
        
    def dfs(self, node, curr, target):
        if node is None:
            return
        
        curr += node.val
        self.cnt += self.map[curr - target]
        self.map[curr] += 1
        self.dfs(node.right, curr, target)
        self.dfs(node.left, curr, target)
        self.map[curr] -= 1
        
        
    
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        
        self.map[0] = 1
        self.dfs(root, 0, targetSum)
        return self.cnt
    
#     # Method 2
#      def pathSum(self, root, targetSum):
#         if root is None:
#             return 0
        
#         # 定义DFS函数，计算以当前节点为起点，路径和等于targetSum的路径数
#         def dfs(node, targetSum):
#             if node is None:
#                 return 0
#             current = node.val
#             totalPaths = 0
#             # 如果当前节点值等于targetSum，则找到一条满足条件的路径
#             if current == targetSum:
#                 totalPaths += 1
#             # 递归计算左子树和右子树中的路径数，并更新targetSum
#             totalPaths += dfs(node.left, targetSum - current)
#             totalPaths += dfs(node.right, targetSum - current)
            
#             return totalPaths
        
#         # 计算以当前节点为起点的所有路径和等于targetSum的路径数
#         pathsFromRoot = dfs(root, targetSum)
#         # 递归计算左子树中的满足条件的路径数
#         pathsOnLeft = self.pathSum(root.left, targetSum)
#         # 递归计算右子树中的满足条件的路径数
#         pathsOnRight = self.pathSum(root.right, targetSum)
        
#         # 返回总的满足条件的路径数
#         return pathsFromRoot + pathsOnLeft + pathsOnRight