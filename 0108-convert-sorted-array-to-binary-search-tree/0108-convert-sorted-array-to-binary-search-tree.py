# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def build(self, start, end, nums):
        if start > end:
            return
        
        mid = start + (end - start) // 2
        root = TreeNode(nums[mid])
        root.left = self.build(start, mid - 1, nums)
        root.right = self.build(mid + 1, end, nums)
        
        return root
        
        
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        return self.build(0, len(nums) - 1, nums)