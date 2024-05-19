class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        """
        通过维护当前最小价格和最大利润来实现
        一个指针记录当前最低的买入价格，另一个指针遍历每一天的价格，并计算可能的最大利润。
        滑动窗口：窗口的左边界是最小的买入价格，右边界是当前价格。
        """

        min_price = 10010
        max_profit = 0
        
        for price in prices:
            # 更新当前最低价格
            if price < min_price:
                min_price = price
            curr_profit = price - min_price
            # 更新最大利润
            if curr_profit > max_profit:
                max_profit = curr_profit
        return max_profit
            
            
            
            
        
        
        
        
            