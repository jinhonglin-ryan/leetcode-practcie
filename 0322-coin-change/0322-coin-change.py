class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        # 完全背包问题
        # 有N个物品和容量是V的背包，每个物品有无限件可用
        # 第i个物品的体积是vi，价值是wi
        # 求将哪些物品装进背包，可以使得物品的总体积不超过背包，且总价值最大
        
        # 这题只需要把每个coin的金额想成体积，每个coin的价值为1，amount想成背包容量，求放满背包的最小价值即可
        # dp[i][j] 为考虑前i个coins凑成j块钱的最少硬币数
        # i.e. 考虑前i个coins凑成amount钱的最少硬币数

        
        n = len(coins)
        m = amount 
        
        # 因为是求min，所以要初始化成最大值, float('inf')
        # 如果是一般的完全背包问题，dp是初始化成0，最小值
        dp = [[float('inf') for _ in range(m + 1)] for _ in range(n + 1)]
        
        # 初始化：当金额为0，无论考虑多少个硬币，都只需要0个就可以凑成这个金额
        for i in range(n + 1):
            dp[i][0] = 0
        
        # 枚举考虑的物品个数（硬币个数）
        for i in range(1, n + 1):
            for j in range(0, m + 1): # 枚举背包容量
                
                # 不选第i个硬币的情况
                dp[i][j] = dp[i - 1][j]
                
                if j >= coins[i - 1]:
                    dp[i][j] = min(dp[i][j], dp[i][j - coins[i - 1]] + 1)
                    
        return dp[n][m] if dp[n][m] != float('inf') else -1
            

            
        
        