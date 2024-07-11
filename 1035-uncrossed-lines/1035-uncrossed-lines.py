class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        
        # 最长公共子序列
        # 与1143一样
        
        # dp[i][j] 表示 nums1前i个数 和 nums2前j个数 的最长公共子序列
        # 返回dp[n][m]
        n = len(nums1)
        m = len(nums2)
        
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, m +1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                    
        return dp[n][m]