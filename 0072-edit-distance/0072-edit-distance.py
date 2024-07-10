class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        # DP
        
        # dp[i][j] 表示word1前i个字符操作后和word2前j个字符相等 的最少步骤
        # 返回dp[n][m]
        
        # dp[i][j] 的递推公式:
        # 1. 如果word1 第i个字符和word2 第j个字符相等，什么操作也不用，dp[i][j] = dp[i - 1][j - 1]
        
        # 2. else:
        
        # a. 插入操作
        #   （1）对word1进行插入操作，即word1前i个字符与word2前j-1个字符相等，插入字符后与word2前j个字符相等，步数+1, dp[i][j] = dp[i][j - 1] + 1
        #    (2) 对word2进行插入操作，即word2前j个字符与word1前i-1个字符相等，插入后与word1前i个字符相等，步数+1, dp[i][j] = dp[i - 1][j] + 1
        
        # b. 删除操作
        #    (1) 对word1进行删除操作，即word1前i-1个字符与word2前j个字符相等，只用删除word1的第i个字符，步数+1，dp[i][j] = dp[i - 1][j] + 1 （与a2相同的递推公式）
        #    (2) 对word2进行删除操作，即word2前j-1个字符与word1前i个字符相等，只用删除word2的第j个字符，步数+1，同理dp[i][j] = dp[i][j - 1] + 1 （与a1相同的递推公式）
        
        # c. 替换操作：
        #    (1) 对word1或者word2当前字符进行替换，替换后相等。对替换word1举例：即word1的前i-1个字符与word2的前j-1个字符已经相等，只需要替换word1的第i个字符为word2的第j个字符即可，dp[i][j] = dp[i - 1][j - 1] + 1
        
        # 总结，递推公式为
        # 如果word1 第i个字符和word2 第j个字符相等，dp[i][j] = dp[i - 1][j - 1]
        # 如果不等：
        # dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)
        
        n = len(word1)
        m = len(word2)
        
        dp = [[float('inf') for _ in range(m + 1)] for _ in range(n + 1)]
        
        # 初始化，观察递推公式，我们是从左上角推到右下角，因此第一行第一列需要初始化
        dp[0][0] = 0
        
        # word1的前i个字符凑成空字符串，全删除即可，操作次数为i
        for i in range(1, n + 1):
            dp[i][0] = i 
            
        # 同理
        for j in range(1, m + 1):
            dp[0][j] = j
            
            
        # 循环遍历
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                    
                else:
                    dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)
                    
                    
        return dp[n][m]
        
        