class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # 完全背包
        # 将n看作背包容量
        # 将1，4，9，16，25...看成物品
        # dp[n] 表示 把物品放入背包，体积不超过n，需要的最少个数
        
        # 物品的最大值为，sqrt(n)，比如n=16，那么我们物品一定要遍历到16
        
        nums = [i * i for i in range(1, int(sqrt(n)) + 1)]
        
        dp = [float('inf') for _ in range(n + 1)]
        
        # 组成 0 不需要任何平方数
        dp[0] = 0
        
        
        for num in nums:
            for j in range(num, n + 1):
                dp[j] = min(dp[j], dp[j - num] + 1)
        
        # 如果dp[n] = 初始化到值，表示没有找到任何组合，返回-1
        return dp[n] if dp[n] != float('inf') else -1 