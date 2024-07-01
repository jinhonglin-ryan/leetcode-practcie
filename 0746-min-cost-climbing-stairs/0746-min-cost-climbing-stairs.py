class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
        # dp 问题
        # 跳到 下标 0 或者 下标 1 是不花费体力的， 从 下标 0 下标1 开始跳就要花费体力了，分别花费为cost[0] 和 cost[1]
        # dp[i] 表示跳到第i台阶所花费的最少体力
        # 这可被分成两个子问题：从i-1和i-2的位置跳
        # dp[i - 1] 跳到 dp[i] 需要花费 dp[i - 1] + cost[i - 1]。dp[i - 2] 跳到 dp[i] 需要花费 dp[i - 2] + cost[i - 2]。
        # dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        
        n = len(cost)
        
        f = [0 for _ in range(n + 1)]

        f[0] = 0
        f[1] = 0
    
        for i in range(2, n + 1):
            f[i] = min(f[i - 1] + cost[i - 1], f[i - 2] + cost[i - 2])
        
        # 
        return f[n]
        