class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        # Method 1. DP
        # dp[i][j] 表示 s 的前 i 个字符是否是 t 的前 j 个字符的子序列。
        # 返回 dp[n][m]
        n = len(s)
        m = len(t)
        
        dp = [[False for _ in range(m + 1)] for _ in range(n + 1)] 
        
        # 初始化 dp 数组
        # s 为空字符串时，它是任何字符串的子序列
        for j in range(m + 1):
            dp[0][j] = True
            
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        
        return dp[n][m]
        
        # # Method 2. 双指针
        # i, j = 0, 0
        # while i < len(s) and j < len(t):
        #     if s[i] == t[j]:
        #         i += 1
        #     j += 1
        # return i == len(s)