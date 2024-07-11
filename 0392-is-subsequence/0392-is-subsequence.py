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
                if s[i-1] == t[j-1]: # 如果 s 的第 i 个字符和 t 的第 j 个字符匹配。
                    # 如果 s 的前 i-1 个字符是 t 的前 j-1 个字符的子序列，那么 s 的前 i 个字符就是 t 的前 j 个字符的子序列。
                    dp[i][j] = dp[i-1][j-1]
                else: #  如果 s 的第 i 个字符和 t 的第 j 个字符不匹配。
                    dp[i][j] = dp[i][j-1] # 我们不能将 t 的第 j 个字符包括在子序列中，那么我们需要看 t 的前 j-1 个字符是否可以包含 s 的前 i 个字符。如果 s 的前 i 个字符是 t 的前 j-1 个字符的子序列，那么 s 的前 i 个字符也会是 t 的前 j 个字符的子序列。继承下来，直到遍历到下一次 i
        
        return dp[n][m]
        
        
        # # Method 2. 双指针
        # i, j = 0, 0
        # while i < len(s) and j < len(t):
        #     if s[i] == t[j]:
        #         i += 1
        #     j += 1
        # return i == len(s)