class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Method 1. 贪心
        # 从头往后遍历，计算连续和，如果连续和变成负数，立刻抛弃，从下一个位置作为起点开始
        res = -float('inf')
        curr_sum = 0
        
        for num in nums:
            curr_sum += num
            if curr_sum > res:
                res = curr_sum
            
            if curr_sum < 0:
                curr_sum = 0 
                
        return res
            
        
        
        # Method 2. DP
        
#         # dp[i] 为以index i 元素结尾的子数组的最大和
#         # 返回 max(dp)
        
#         # 对于每个元素 nums[i]，我们有两个选择：
#         # 1. 只包含 nums[i] 这个元素，作为一个新的子数组的开始。
#         # 2. 将 nums[i] 加入到前面计算出的最大子数组和中。
        
#         n = len(nums)
#         dp = [0 for _ in range(n)]
        
#         dp[0] = nums[0]
        
#         for i in range(1, n):
#             dp[i] = max(nums[i], dp[i - 1] + nums[i])
            
#         return max(dp)