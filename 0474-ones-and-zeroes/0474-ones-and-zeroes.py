class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        
        # 01 背包
        # 背包容量有两个维度 有多少个1和多少个0
        
        # dp[i][j] 表示装满i个0和j个1容量的背包 最多装了dp[i][j]个物品
        # 返回dp[m][n]
        
        # 递推公式：01背包的基础递推公式为
        # dp[j] = max(dp[j], dp[j - weight[i]] + value[i]) 求的放满j获得的最大价值
        # 这里因为背包容量有两个维度，所以需要一个二维dp数组
        # 且这里求的是放满背包容量，需要的最大数量，所以每个string的价值都是1，表示个数
        
        
        
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        for substr in strs: # 遍历物品
            x = 0 # 记录substr中的部分重量，即0有多少个
            y = 0 # 记录substr中的部分重量，即1有多少个
            for ch in substr:
                if ch == '0':
                    x += 1
                else:
                    y += 1
                    
            # 倒叙遍历背包容量，因为有容量两层维度，所以双重循环
            
            for i in range(m, x - 1, -1):
                for j in range(n, y - 1, - 1):
                    dp[i][j] = max(dp[i][j], dp[i - x][j - y] + 1)
                    
        return dp[m][n]
            