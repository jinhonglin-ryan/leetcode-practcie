class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        # Method 1. 状态机DP
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
            
            # 第i天结束时，持有股票的最大利润为：延续前一天的持有 或者 前一天不持有 今天刚买入（但是我们知道只能交易一次，所以前一天不持有的最大利润为0, 所以是-prices[i]）
            dp[i][1] = max(dp[i - 1][1], -prices[i])
            
            
        return max(dp[n - 1][0], dp[n - 1][1])
        
        
        
#         # Method 2. Sliding Window
#         """
#         通过维护当前最小价格和最大利润来实现
#         一个指针记录当前最低的买入价格，另一个指针遍历每一天的价格，并计算可能的最大利润。
#         滑动窗口：窗口的左边界是最小的买入价格，右边界是当前价格。
#         """

#         min_price = 10010
#         max_profit = 0
        
#         for price in prices:
#             # 更新当前最低价格
#             if price < min_price:
#                 min_price = price
#             curr_profit = price - min_price
#             # 更新最大利润
#             if curr_profit > max_profit:
#                 max_profit = curr_profit
#         return max_profit
            
            
            
            
        
        
        
        
            