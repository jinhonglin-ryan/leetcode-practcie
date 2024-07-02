class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # 与198类似，只不过多个分类讨论，现在是一个环形
        # 198说的是在[0, n-1]的最大值
        # 1. 第一个位置必选：则最后一个位置必不能选：返回的是g1[n - 1]
        # 2. 第一个位置不选：则最后一个位置可选可不选：返回的是 max(f2[n - 1], g2[n -1])
        # 则这道题是要考虑在[0, n-2]的最大值（选第一个的情况）
        # 和[1, n-1]的最大值（不选第一个情况）
        
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 0:
            return 0
        
        def rob_helper(start, end):
            f = [0 for _ in range(n)]
            g = [0 for _ in range(n)]
            
            f[start] = nums[start]
            g[start] = 0 
            
            for i in range(start + 1, end + 1):
                f[i] = g[i - 1] + nums[i]
                g[i] = max(f[i-1], g[i-1])
                
            return max(f[end], g[end])
        
        rob_first = rob_helper(0, n - 2)
        not_rob_first = rob_helper(1, n - 1)
        
        return max(rob_first, not_rob_first)
            