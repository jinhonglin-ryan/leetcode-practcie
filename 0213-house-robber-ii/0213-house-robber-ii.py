class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 与198类似，只不过多个分类讨论，现在是一个环形
        # 198说的是在[0, n-1]的最大值，这道题的分类讨论如下
        # 1. 选第一个：考虑在[0, n-2]的最大值
        # 2. 不选第一个：考虑在[1, n-1]的最大值
        
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        
        # 分类讨论1：不选第一个，则在[1, n -1] 找最大值（最后一位可选可不选）
        f1 = [0 for _ in range(n)]
        g1 = [0 for _ in range(n)]
        
        f1[1] = nums[1]
        g1[1] = 0
        
        for i in range(2, n):
            f1[i] = g1[i - 1] + nums[i]
            g1[i] = max(f1[i-1], g1[i-1])
            
        rob_first = max(f1[n - 1], g1[n - 1])
        
        
        # 分类讨论2：选第一个，则在[0, n - 2]找最大值 （最后一位必不选）
        f0 = [0 for _ in range(n)]
        g0 = [0 for _ in range(n)] 
        
        f0[0] = nums[0]
        g0[0] = 0
        
        for i in range(1, n - 1):
            f0[i] = g0[i - 1] + nums[i]
            g0[i] = max(f0[i-1], g0[i-1])
            
        not_rob_first = max(f0[n-2], g0[n-2])
        
        return max(rob_first, not_rob_first) 
        
        
        # 与198类似，只不过多个分类讨论，现在是一个环形
        # 198说的是在[0, n-1]的最大值，这道题的分类讨论如下
        # 1. 选第一个：考虑在[0, n-2]的最大值
        # 2. 不选第一个：考虑在[1, n-1]的最大值
        
#         n = len(nums)
#         if n == 1:
#             return nums[0]
#         if n == 0:
#             return 0
        
#         def rob_helper(start, end):
#             f = [0 for _ in range(n)]
#             g = [0 for _ in range(n)]
            
#             f[start] = nums[start]
#             g[start] = 0 
            
#             for i in range(start + 1, end + 1):
#                 f[i] = g[i - 1] + nums[i]
#                 g[i] = max(f[i-1], g[i-1])
                
#             return max(f[end], g[end])
        
#         rob_first = rob_helper(0, n - 2)
#         not_rob_first = rob_helper(1, n - 1)
        
#         return max(rob_first, not_rob_first)

        
        
            