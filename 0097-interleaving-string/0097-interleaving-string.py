class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        
        # DP
        
        # dp[i][j] 表示s1的前个字符和s2的前j个字符能否凑成s3的前i+j个字符
        # 因此dp[i][j] 取决于：s3的第i+j个字符是
        # 1. 等于s1的第i个字符，且dp[i - 1][j] 为true，即s1的前i-1个字符和s2的前j个字符可以凑成s3的前i+j-1个字符，那么dp[i][j]为true 
        # 或者是
        # 2. 等于s2的第j个字符，且dp[i][j - 1]为true 分析同理
        
        n = len(s1)
        m = len(s2)
        
        if n + m != len(s3):
            return False 
        
        dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]
        
        # 初始化
        dp[0][0] = True # 空字符串可以凑成空字符串
        
        # 观察递推公式，我们是从左上角推到右下角，因此需要初始化第一行第一列
        for i in range(1, n + 1):
            dp[i][0] = s1[i - 1] == s3[i - 1] and dp[i - 1][0]
            
        for j in range(1, m + 1):
            dp[0][j] = s2[j - 1] == s3[j - 1] and dp[0][j - 1]
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                case_1 = s1[i - 1] == s3[i + j - 1] and dp[i - 1][j]
                case_2 = s2[j - 1] == s3[i + j - 1] and dp[i][j - 1]
                
                dp[i][j] = case_1 or case_2
                
        return dp[n][m]
        
        