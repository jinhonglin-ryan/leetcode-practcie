class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 状态机DP
        # 一共两种状态，即第i天持有，或不持有，用第二个index 1/0 表示
        # dp[i][1] 表示 第 i 天结束时，持有股票的最大利润（包括当天买入 or 持续持有）
        # dp[i][0] 表示 第 i 天结束时，不持有股票的最大利润（包括当天卖出 or 持续不持有）
        # 返回dp[n - 1][0] 和 dp[n - 1][1] 的最大值，即最后一天结束时 持有/不持有的最大利润
        
        # 初始化
        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(n)]
        
        # 第0天结束时，不持有股票代表什么也没干，利润为0
        # 第0天结束时，持有股票代表这一天买入了，利润为负的当天价格
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        
        # 从第一天起遍历
        for i in range(1, n):
            # 第i天结束时，不持有股票的最大利润为：延续前一天的不持有 or 前一天持有，今天卖出
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            
            # 第i天结束时，持有股票的最大利润为：延续前一天的持有 或者 前一天不持有 今天刚买入（与121不同的是，前一天的持有在这里是有利润的，利润是dp[i - 1][0]）
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0]-prices[i])
            
            
        return max(dp[n - 1][0], dp[n - 1][1])
        