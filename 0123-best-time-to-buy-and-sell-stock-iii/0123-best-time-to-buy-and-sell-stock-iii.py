class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        # 状态机DP
        # 121 只能交易一次
        # 122 可以无限次交易
        # 这题 只能交易2次
        
        # 定义
        # dp[i][0] 为第i天结束时 没有做任何操作   手头的最大利润
        # dp[i][1] 为第i天结束时 第一次持有股票   手头的最大利润
        # dp[i][2] 为第i天结束时 第一次不持有股票 手头的最大利润
        # dp[i][3] 为第i天结束时 第二次持有股票   手头的最大利润
        # dp[i][4] 为第i天结束时 第二次不持有股票 手头的最大利润
        
        n = len(prices)
        dp = [[0 for _ in range(5)] for _ in range(n)]
        
        dp[0][0] = 0            # 第0天结束没有干任何事情，利润为0
        dp[0][1] = -prices[0]   # 第0天结束第一次买入，起始是没有钱的，利润为-prices[0]
        dp[0][2] = 0            # 第0天结束第一次买入第一次卖出，同样的价格，利润为0
        dp[0][3] = -prices[0]   # 第0天结束第一次买入第一次卖出后，又买一次，利润为-prices[0]
        dp[0][4] = 0            # 第0天结束第一次买入第一次卖出第二次买入后，又卖了，同样的价格，利润为0
        
        for i in range(1, n):
            # 第i天结束什么也没干，手头利润跟前一天一样
            dp[i][0] = dp[i - 1][0]
            
            # 第i天结束还是属于第一次持有股票，可以属于前一天的延续，或者是前一天什么也没干，然后第i天买入
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            
            # 第i天结束还是属于第一次不持有股票，可以属于前一天的延续，或者是前一天为第一次持有股票，第i天卖出
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + prices[i])
            
            # 第i天结束还是属于第二次持有股票，可以属于前一天的延续，或者前一天是第一次不持有股票，第i天买入
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] - prices[i])
            
            # 第i天结束还是属于第二次不持有股票，可以属于前一天的延续，或者是前一天是第二次持有股票，第i天卖出
            dp[i][4] = max(dp[i - 1][4], dp[i - 1][3] + prices[i])
            
        
        return max(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2], dp[n - 1][3], dp[n - 1][4])