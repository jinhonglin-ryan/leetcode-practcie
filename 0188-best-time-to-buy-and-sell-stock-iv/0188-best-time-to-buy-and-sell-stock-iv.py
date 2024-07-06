class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        
        # 状态机DP
        # 类似123（至多买卖2次）
        # 123 买卖两次的状态有1 + 2 * 2 是5个，分别对应1：不操作 和 两次买入和 两次卖出
        # 因此我们至多买卖k次的状态有2k + 1 个
        
        n = len(prices)
        dp = [[0 for _ in range(2 * k + 1)] for _ in range(n)]
        
        # j为奇数的时候，是我们第0天结束时买入的状态，因此钱为负的
        # j为0和偶数的时候，是我们第0天结束时 不操作 或者 卖出的状态，钱为0 在声明dp数组时已经声明好了
        for j in range(1, 2 * k + 1, 2):
            dp[0][j] = -prices[0]
            
            
        for i in range(1, n):
            # 如果第i天结束时什么也没干，手头利润跟前一天一样
            dp[i][0] = dp[i - 1][0]
            
            # 遍历第j次交易的情况
            for j in range(0, 2 * k, 2):
                # 仿照123代码写出的
                # 如果第i天结束时是第j次持有股票，那么要么是延续前一天的利润，继续持有，或者前一天是不持有股票的，第i天买入
                dp[i][j + 1] = max(dp[i - 1][j + 1], dp[i - 1][j] - prices[i])
                
                # 如果第i天结束时是第j次不持有股票，那么要么是延续前一天的利润，继续不持有，或者是前一天是持有的，第i天卖出
                dp[i][j + 2] = max(dp[i - 1][j + 2], dp[i - 1][j + 1] + prices[i])
                
        
        max_res = -10000
        for j in range(0, 2* k + 1):
            if dp[n - 1][j] > max_res:
                max_res = dp[n - 1][j]

        return max_res 
        
                
        
 