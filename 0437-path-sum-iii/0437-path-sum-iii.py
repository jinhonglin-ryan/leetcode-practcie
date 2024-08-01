# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    # Method 1. 前缀和 + 哈希表
    def __init__(self):
        self.cnt = 0
        self.prefixSum = defaultdict(int)
    
    def dfs(self, node, currSum, targetSum):
        if node is None:
            return
        
        # 从根到当前node的总和是currSum
        currSum += node.val
        
        # 我们需要知道在这条路径上有多少条路径等于targetSum, 所以就需要知道currSum - targetSum在哈希表中出现过几次
        self.cnt += self.prefixSum[currSum - targetSum]
        
        # 更新当前路径和的前缀和计数
        self.prefixSum[currSum] += 1
        
        # 递归处理左子树和右子树
        self.dfs(node.left, currSum, targetSum)
        self.dfs(node.right, currSum, targetSum)
        
        # 回溯，恢复当前路径和的前缀和计数
        self.prefixSum[currSum] -= 1
        
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        self.prefixSum[0] = 1 # 哨兵
        self.dfs(root, 0, targetSum) # 修正初始参数顺序
        return self.cnt