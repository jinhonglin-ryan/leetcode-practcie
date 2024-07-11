class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # dp[i] 为以第 i 个元素结尾的子数组的最大和
        # 返回 max(dp)
        
        n = len(nums)
        dp = [0 for _ in range(n)]
        
        dp[0] = nums[0]
        
        max_sum = nums[0]  # 初始化 max_sum 为 nums[0]

        for i in range(1, n):
            # dp[i] 的值取决于 nums[i] 和 dp[i-1] + nums[i] 的较大值
            dp[i] = max(nums[i], dp[i-1] + nums[i])
            # 更新 max_sum
            max_sum = max(max_sum, dp[i])

        return max_sum