class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        n = len(s)
        if n == 0:
            return 0
        
        if n == 1:
            return 1
        
        dp = [[False for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = True
        
        count = n 
        for j in range(1, n):
            for i in range(j):
                if s[i] == s[j]:
                    if j - i <= 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False 
                    
                if dp[i][j]:
                    count += 1
                        
        
        
        return count