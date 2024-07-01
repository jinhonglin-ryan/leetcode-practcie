class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # dp问题
        # 从第0级台阶开始，到第1级台阶我们有1种方法
        # 到第n级台阶有几种方法可以分类讨论
        # 1. 是从第n-1级台阶跳一次跳到n级
        # 2. 是从第n-2级台阶跳两次跳到n级
        # 所以到第n级台阶有几种走法 =  n-1 走法 + n-2 走法
        
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]