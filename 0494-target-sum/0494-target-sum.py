class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Method 1. DP 01背包
        # 可以把nums分成准备加入+号的集合 和 准备加入-号的集合
        # 准备加入+号的集合的和为left, 准备加入-号的集合的和为right 
        # 我们得出等式 left + right = sum, 且 在题目要求的情况下，left - right = target
        # 得出left = (sum + target) / 2
        # 如果整除失败，说明没有这样一个left集合存在，return 0 即可
        # 整除成功，问题就变成了，我们将nums里的数字放入背包，其容量大小为left，有多少种方法
        
        # 定义dp[j] 为 装满背包容量为j，有dp[j]种 <方法>
        # 所以递推公式为 dp[j] += dp[j - nums[i]]   (求组合类问题的公式)
        # 只要搞到 nums[i]，凑成 dp[j] 就有 dp[j - nums[i]] 种⽅法。例如
        # dp[j]，j 为 5
        # 已经有⼀个 1（nums[i]）的话，有 dp[4] 种⽅法凑成容量为 5 的背包。
        # 已经有⼀个 2（nums[i]）的话，有 dp[3] 种⽅法凑成容量为 5 的背包。
        # 凑成dp[5]的话就是把所有dp[5 - nums[i]] 累加起来
        
        # 初始化 dp[0] = 1 即凑成背包容量为0的方法只有1种，什么也不干
        # 从递推公式来看，当前我们的物品体积为5，bagsize也是5，那么dp[5] = dp[5 - 5] = dp[0]
        # dp[0] 要等于1 才能满足有1种方法凑成dp[5], 即直接放入5这个数
        
        sum_sum = sum(nums)
        
        if sum_sum < abs(target): # 如果全加/全减也没有办法凑成target
            return 0 
        
        elif (sum_sum + target) % 2 != 0: # 如果没有办法partition出一个+号集合 和 -号集合
            return 0
        
        else:
            bagsize = (sum_sum + target) // 2
            
        dp = [0 for _ in range(bagsize + 1)]
        
        dp[0] = 1
        
        for i in range(len(nums)):
            for j in range(bagsize, nums[i] - 1, -1):
                # 不使用当前元素 dp[j]
                # 使用当前元素：方法数 = 填满 容量 j - nums[i]的方法数，再加上当前nums[i]
                dp[j] = dp[j] + dp[j - nums[i]]
                
        return dp[bagsize]
        
        
        
#         # Method 2. DFS 超时
#         def dfs(index, curr_sum):
#             if index == len(nums):
#                 if curr_sum == target:
#                     return 1
#                 else:
#                     return 0
                
#             # 分别找尝试+号和尝试-号的方法数
#             ans = dfs(index + 1, curr_sum + nums[index]) + dfs(index + 1, curr_sum - nums[index]) 
            
#             return ans
            
#         return dfs(0, 0)