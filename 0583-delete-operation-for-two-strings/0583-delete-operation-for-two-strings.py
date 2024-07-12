class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        # dp[i][j] 表示word1前i个字符 和word2前j个字符 操作后相等 的最少步骤
        # 返回dp[n][m]
        
        # 递推公式：如果当前两个字符相等，什么都不用操作 dp[i][j] = dp[i - 1][j - 1]
        # 如果当前两个字符不相等，需要删除操作，有三种删的方法，取最小值
        # 删除当前word1的字符，即看 word1 前 i - 1个字符 和 word2 前j个字符 操作后相等的最小步骤，步数+1 为dp[i][j]
        # 删除当前word2的字符，步数+1 为dp[i][j]
        # 删除当前word1 和 word2 的字符，步数+2 为 dp[i][j]
        
        n = len(word1)
        m = len(word2)
        
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        
        # 初始化 word1前i个字符 和 word2的空字符 相等，需要删除word1 i次
        for i in range(n + 1):
            dp[i][0] = i
            
        # 同理
        for j in range(m + 1):
            dp[0][j] = j 
            
            
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 2)
                    
        return dp[n][m]
    
     