class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        m = amount 
        
        dp = [float('inf') for _ in range(amount + 1)]
        
        dp[0] = 0
        
        
        n = len(coins)
        
        
        for i in range(n):
            for j in range(coins[i], m + 1):
                dp[j] = min(dp[j], dp[j - coins[i]] + 1)
                
                
        return dp[amount] if dp[amount] != float('inf') else -1 