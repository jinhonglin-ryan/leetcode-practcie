class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # 完全背包DP，求排列
        
        # 在求装满背包有几种方式时，遍历顺序很关键
        # 求组合：外层物品，内层背包容量，从小到大
        # 求排列，外层背包，内层物品
        
        
        # dp[j]: 装满容量为j的背包，有dp[j]种方法
        # 返回dp[target]
        
        # 递推公式：dp[j] += dp[j - nums[i]]   (求装满背包有多少种方法 问题的公式)
        
        dp = [0 for _ in range(target + 1)]
        
        dp[0] = 1
        
        for j in range(target + 1): # 外层遍历背包容量 
            for i in range(len(nums)): # 内层遍历物品
                if j >= nums[i]:
                    dp[j] += dp[j - nums[i]]
                
        return dp[target]