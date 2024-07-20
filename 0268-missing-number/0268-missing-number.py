class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Method 1. yxc
        # 0 - n 个数的和是 (0 + n) * (n + 1) / 2
        # 减去nums的和，就是缺失的数
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)
        
#         # Method 2. 排序
#         n = len(nums)
#         nums = sorted(nums)
        
#         for i in range(n):
#             if nums[i] != i:
#                 return i
            
#         return i + 1