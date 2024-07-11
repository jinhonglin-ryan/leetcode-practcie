class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        
        # dp[i][j] 为 以 nums1[i-1] 和 nums2[j-1] 结尾的最长公共子数组的长度。 
        # 返回dp数组中最大的值
        # 而不是返回dp[n][m]: 直接返回 dp[n][m] 的假设是，最长的公共子数组会出现在 nums1 和 nums2 的结尾。然而，最长公共子数组可能出现在这两个数组的中间部分，而不是在结尾。
        # 比如例子 nums1 = [12321] nums2 = [32147]
        # dp[5][3] 就是考虑 12321 和 321 的重复子数组最长长度，就是3
        # 而不是return dp[5][5], 因为公共子数组并不是出现在nums2的结尾
        
        
        n = len(nums1)
        m = len(nums2)
        
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        
        dp[0][0] = 0
        ans = 0 
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # 表示当前元素可以延续之前的公共子数组。
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else: # 当前元素不能构成公共子数组
                    dp[i][j] = 0
                    
                # 找出最大值   
                if dp[i][j] > ans:
                    ans = dp[i][j]
        # 我们需要找出整个 dp 数组中的最大值，因为最长的公共子数组可能出现在 nums1 和 nums2 的任何位置，而不仅仅是在结尾。
        return ans