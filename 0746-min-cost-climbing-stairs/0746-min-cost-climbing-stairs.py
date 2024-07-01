class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
        # dp 问题
        # f[i] 表示跳到i的最小cost
        # 这可被分成两个子问题：到第 i - 1 个台阶所花费的最小cost 与 到第 i - 2 个台阶所花费的最小cost中的 最小值 + 到达第 i 个台阶所需要的cost。
        # f[i] = min(f[i - 1], f[i - 2]) + cost[i]
        
        n = len(cost)
        
        f = [0 for _ in range(n)]
        
        f[0] = cost[0]
        f[1] = cost[1]
        
        for i in range(2, n):
            f[i] = min(f[i - 1], f[i - 2]) + cost[i]
            
        return min(f[n - 2], f[n - 1])
        