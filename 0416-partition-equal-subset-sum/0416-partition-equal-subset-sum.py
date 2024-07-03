class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # 01背包问题
        # dp[i][j] 表示在前 i 个元素中是否可以找到一个子集，使其和为 j。
        # 有n个物品
        # 每个物品的体积相当于每个数的大小，不用考虑每个物品的价值，因为我们只要True or False，看看考虑前i个物品，能不能放入体积为j的背包中
        # 背包容量是sum(nums) / 2 
        
        # 如果我们能把一些数装进一个背包里，那么剩下的数肯定能装进另一个背包里
        
        
        sum_nums = sum(nums)
    
        # 如果背包容量总和是奇数，不可能可以分成两个sum相同的一堆整数和（无法分割成两个和相等的子集
        if sum_nums % 2 != 0:
            return False

        m = sum_nums // 2  # 使用整数除法
        n = len(nums)

        # 初始化 dp 数组，dp[i][j] 表示前 i 个数是否可以组成和为 j
        dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]

        # 在前 i 个元素中，总是可以找到一个和为0的子集
        for i in range(n + 1):
            dp[i][0] = True

        # 遍历物品个数
        for i in range(1, n + 1):
            for j in range(1, m + 1): # 遍历背包容量
                dp[i][j] = dp[i - 1][j]  # 不选第 i 个数

                if j >= nums[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j - nums[i - 1]]  # 选第 i 个数

        return dp[n][m]
