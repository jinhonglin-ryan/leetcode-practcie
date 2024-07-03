class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # DP问题
        # dp[i] 表示为：以nums[i] 结尾的最长递增子序列长度。
        # dp[n - 1]为返回答案
        # 初始化dp所有entry为1，即自己本身


        n = len(nums)
        dp = [1 for _ in range(n)]
        
        # 一般遍历，外层遍历终点，内层遍历起点
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    
        return max(dp)
        
        
            