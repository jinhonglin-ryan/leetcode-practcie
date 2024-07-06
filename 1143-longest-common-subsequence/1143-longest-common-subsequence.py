class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        
        # 二维dp
        # dp[i][j] 存的是 text1 前i个字符 和 text2 前j个字符 所有公共子序列最长的那个 的长度
        # 返回 dp[n][m]
        
        n = len(text1)
        m = len(text2)
        
        # dp[0][j] 和 dp[i][0] 都为0，因为和空字符串的最长公共子序列的长度都为0 
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        
        # 一般的双重循环 遍历text1 和 text2 的所有字符，来填充dp表（一行一行填充）
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # 如果当前两个字符相同，那么当前两个字符可以作为最长公共子序列的一部分，所以dp[i][j] = dp[i - 1][j - 1] + 1
                # index 从1开始，所以要取到当前字符，需要 - 1
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                
                # 否则的话，取前一个状态的最大值
                # 即第i个字符在最长子序列里，第j个字符在最长子序列里，或者两者都不在
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                    
        return dp[n][m]