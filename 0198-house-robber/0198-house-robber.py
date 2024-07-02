class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # f[i] 为必选i个位置的所有组合中的最大profit: 即不选i-1个位置的最大profit + 第i个位置的profit 
        # g[i] 为不选i个位置的所有组合中的最大profit: 即不选i-1个位置的最大profit 和 选i-1个位置的最大profit 的最大值
        
        # f[i] = g[i - 1] + nums[i] 
        # g[i] = max(g[i-1], f[i-1])
        
        n = len(nums)
        
        f = [0 for _ in range(n)]
        g = [0 for _ in range(n)]
        
        f[0] = nums[0]
        g[0] = 0
        
        for i in range(1, n):
            f[i] = g[i - 1] + nums[i]
            g[i] = max(g[i - 1], f[i - 1])
        
        return max(f[n - 1], g[n - 1])
            