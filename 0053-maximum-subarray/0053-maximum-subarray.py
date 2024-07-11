class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # dp[i] 为以第 i 个元素结尾的子数组的最大和
        # 返回 max(dp)
        
        # 对于每个元素 nums[i]，我们有两个选择：
        # 1. 只包含 nums[i] 这个元素，作为一个新的子数组的开始。
        # 2. 将 nums[i] 加入到前面计算出的最大子数组和中。
        
        n = len(nums)
        dp = [0 for _ in range(n)]
        
        dp[0] = nums[0]
        
        for i in range(1, n):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
            
        return max(dp)