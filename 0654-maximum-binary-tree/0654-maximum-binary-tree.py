# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        if not nums:
            return None

        # 找到数组中的最大值及其索引
        maxNum = nums[0]
        maxIndex = 0
        for i in range(1, len(nums)):
            if nums[i] > maxNum:
                maxNum = nums[i]
                maxIndex = i
        
        # 创建根节点
        root = TreeNode(maxNum)
        
        # 构建左子树
        if maxIndex > 0:
            root.left = self.constructMaximumBinaryTree(nums[:maxIndex])
        
        # 构建右子树
        if maxIndex < len(nums) - 1:
            root.right = self.constructMaximumBinaryTree(nums[maxIndex+1:])
        
        return root