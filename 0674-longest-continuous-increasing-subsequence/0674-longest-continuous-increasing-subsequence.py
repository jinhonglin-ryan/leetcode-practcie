class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # DP
        # 以下标i为结尾的连续递增的子序列⻓度为dp[i]。
        # 返回dp数组的最大值即可 
        
        n = len(nums)
        dp = [0 for _ in range(n)]
        
        dp[0] = 1
        
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1
                
            else:
                dp[i] = 1
                
                
        return max(dp)