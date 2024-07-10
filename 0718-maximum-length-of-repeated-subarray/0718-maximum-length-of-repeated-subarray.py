class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        
        # dp[i][j] 为 nums1的前i个数 和 nums2的前j个数 重复子序列的最长长度
        
        
        n = len(nums1)
        m = len(nums2)
        
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        
        dp[0][0] = 0
        ans = 0 
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    
                if dp[i][j] > ans:
                    ans = dp[i][j]
                    
        return ans