class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # 01背包问题 
        # Method 0. 降维
        # 一半的sum看成是背包总容量 m
        # 每个数字看成物品，体积为数值大小，价值也为数值大小
        # dp[j] 定义为容量为j的背包，所背的最大价值为 dp[j]
        # 返回dp[half_sum] == half_sum 即看看容量为half_sum 的背包，所背的最大价值 是不是half_sum
        # 因为每个物品（数字）的体积和价值一样，所以这个等价于 把数字放进容量为half_sum的背包里，这些数字能不能凑成half_sum
        
        sum_sum = sum(nums)
        
        if sum_sum % 2 != 0:
            return False
        
        m = sum_sum // 2
        n = len(nums)
        
        dp = [0 for _ in range(m + 1)]
        
        # 01 背包模板
        for i in range(n): # 遍历物品
            for j in range(m, nums[i] - 1, -1): # 倒叙遍历背包容量，保证每个元素只能放一次，要取到num[i]，所以右端点是nums[i] - 1
                # dp[j] 取「前 i - 1 件物品装入载重为 j 的背包中的最大价值」与「前 i - 1 件物品装入载重为 w - weight[i - 1] 的背包中，再装入第 i 物品所得的最大价值」两者中的最大值
                dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])
        
        return dp[m] == m
                
            
        
        
#         # Method 1.
#         # 一半的sum看成是背包总容量 m
#         # 每个数字看成物品，体积为数值大小，价值也为数值大小
#         # dp[i][j] 表示前i个物品 在总体积不超过背包容量j的情况下，背包里所能达到的价值
#         # 这里价值跟体积是一样的，所以可以被 paraphrase 成 前i个物品放入背包，在总体积不超过背包容量j的情况下，所能达到的最大体积
#         # 返回结果dp[n][m] == m 就是考虑所有的数字，都尝试放入背包中，在体积不超过target sum m的情况下，看看最大体积能不能达到m
#         # 如果最大体积等于m，说明在n个数中存在一些数，放入背包后，体积不超过背包，且体积等于m，说明有解，这个nums数组中存在partition
        
#         sum_sum = sum(nums)
        
#         if sum_sum % 2 != 0:
#             return False
        
#         m = sum_sum // 2
#         n = len(nums)
        
#         dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        
#         # 01背包模板
#         for i in range(1, n + 1):
#             for j in range(m + 1):
                
#                 dp[i][j] = dp[i - 1][j]
                
#                 if j >= nums[i - 1]:
#                     dp[i][j] = max(dp[i][j], dp[i - 1][j - nums[i - 1]] + nums[i - 1])
                    
#         return dp[n][m] == m
    
        
        
        
        
        
#         # 01背包问题
#         # Method 2.
#         # dp[i][j] 表示在前 i 个元素中是否可以找到一个子集，使其和为 j。
#         # 有n个物品
#         # 每个物品的体积相当于每个数的大小，不用考虑每个物品的价值，因为我们只要True or False，看看考虑前i个物品，能不能放入体积为j的背包中
#         # 背包容量是sum(nums) / 2 
        
#         # 如果我们能把一些数装进一个背包里，那么剩下的数肯定能装进另一个背包里
        
        
#         sum_nums = sum(nums)
    
#         # 如果背包容量总和是奇数，不可能可以分成两个sum相同的一堆整数和（无法分割成两个和相等的子集
#         if sum_nums % 2 != 0:
#             return False

#         m = sum_nums // 2  # 使用整数除法
#         n = len(nums)

#         # 初始化 dp 数组，dp[i][j] 表示前 i 个数是否可以组成和为 j
#         dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]

#         # 在前 i 个元素中，总是可以找到一个和为0的子集
#         for i in range(n + 1):
#             dp[i][0] = True

#         # 遍历物品个数
#         for i in range(1, n + 1):
#             for j in range(1, m + 1): # 遍历背包容量
#                 dp[i][j] = dp[i - 1][j]  # 不选第 i 个数， 那么是否能够组成和为 j 的子集就取决于前 i-1 个数是否能够组成和为 j 的子集。

#                 if j >= nums[i - 1]:
#                     dp[i][j] = dp[i][j] or dp[i - 1][j - nums[i - 1]]  # 选第 i 个数， 如果 dp[i - 1][j - nums[i - 1]] 为 True，说明前i-1个数存在子集 可以凑成和为 j-nums[i - 1]，说明我们可以通过选择第 i 个数使和达到 j。
        
#         return dp[n][m]
