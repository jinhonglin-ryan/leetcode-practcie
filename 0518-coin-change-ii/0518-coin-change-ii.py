class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        
        # DP 完全背包，求组合
        # 外层遍历物品，内层遍历背包容量，从小到大
        # dp[j]: 装满容量为j的背包，有dp[j]种方法
        # 返回dp[amount]
        
        # 递推公式：dp[j] += dp[j - nums[i]]   (求装满背包有多少种方法 问题的公式)
        
        # 在求装满背包有几种方式时，遍历顺序很关键
        # 求组合：外层物品，内层背包容量，从小到大
        # 求排列，外层背包，内层物品
        
        dp = [0 for _ in range(amount + 1)]
        
        dp[0] = 1
        
        for i in range(len(coins)):
            for j in range(coins[i], amount + 1):
                dp[j] += dp[j - coins[i]] 
                
                
        return dp[amount]
        