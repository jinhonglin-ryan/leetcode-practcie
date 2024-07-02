class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0 :
            return 0
        
        if n == 1:
            return 1
        
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 1
            
        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = length + i - 1 # length = j - i + 1
                
                if s[i] == s[j]:
                    if length == 1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
                        
             
        return dp[0][n-1]