class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        
        # 01 背包问题
        # 尽量把石头分成大小差不多的两堆
        # 最后两堆重量减一下 就是答案
        # 类似416 分割等和子集
        
        # 每个石头看成物品，体积为重量大小，价值也为重量大小
        # dp[j] 定义为 装满容量为j的背包，所背的最大价值为 dp[j]
        # or          装满容量为j的背包，所背的最大重量为 dp[j]
        
        
        # 尽量分成重量相等的2堆，一堆重量是target，一堆重量是sum-target
        # 然后求出dp[target]的值，即尝试装满target容量的背包，需要的最大石头总重为dp[target]
        # 另一堆就是sum - dp[target]
        # 最后返回绝对值 dp[target] - (sum - dp[target])
        
        target = sum(stones) // 2 
        
        dp = [0 for _ in range(target + 1)]
        
        n = len(stones)
        
        for i in range(n):
            for j in range(target, stones[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])
        
        return abs(dp[target] - (sum(stones) - dp[target]))
        