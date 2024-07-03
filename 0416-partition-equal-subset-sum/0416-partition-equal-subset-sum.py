class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # 01背包问题
        # 有n个物品
        # 每个物品的体积相当于每个数的大小，价值也是每个数的大小
        # 背包容量是sum(nums) / 2 
        
        # 如果我们能把一些数装进一个背包里，那么剩下的数肯定能装进另一个背包里
        
        # 如果背包容量是奇数，不可能可以分成两个sum为相同的一堆整数和
        sum_nums = sum(nums)
    
        # 如果总和是奇数，无法分割成两个和相等的子集
        if sum_nums % 2 != 0:
            return False

        m = sum_nums // 2  # 使用整数除法
        n = len(nums)

        # 初始化 dp 数组，dp[i][j] 表示前 i 个数是否可以组成和为 j
        dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]

        # 容量为 0 的背包可以被任何集合分割
        for i in range(n + 1):
            dp[i][0] = True

        # 填充 dp 数组
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = dp[i - 1][j]  # 不选第 i 个数

                if j >= nums[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j - nums[i - 1]]  # 选第 i 个数

        return dp[n][m]
