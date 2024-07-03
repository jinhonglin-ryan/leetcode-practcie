class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
#         # DP 问题 
#         # f[i] 表示的是以 nums[i] 结尾的所有子数组中，乘积最大的那个子数组的乘积。
#         # g[i] 表示的是以 nums[i] 结尾的所有子数组中，乘积最小的那个子数组的乘积。
        
#         # 在第 i 步时，dp_max[i] 的值可以由以下三种情况决定：

#         # 1. 当前元素 nums[i] 本身。这种情况对应于从当前元素重新开始计算子数组。
#         # 2. f[i - 1] * nums[i]，即前一个位置的最大乘积子数组乘以当前元素。因为当前元素是正数，这种情况会让乘积变大。这意味着当前元素 nums[i] 继续接在前一个位置的最大乘积子数组之后，形成一个新的子数组。
#         # 3. g[i - 1] * nums[i]，即前一个位置的最小乘积子数组乘以当前元素。因为当前元素是负数，这种情况会让乘积变大。
        
        
#         n = len(nums)
        
#         f = [0 for _ in range(n)]
#         g = [0 for _ in range(n)]
        
#         f[0] = nums[0]
#         g[0] = nums[0]
#         res = nums[0]
        
#         for i in range(1, n):
#             a = nums[i]
#             f[i] = max(f[i - 1] * a, a, g[i - 1] * a)
#             g[i] = min(f[i - 1] * a, a, g[i - 1] * a)
#             res = max(res, f[i])
            
#         return res 

        # 滚动优化版本
        n = len(nums)
        f = nums[0]
        g = nums[0]
        res = nums[0]
        
        for i in range(1, n):
            a = nums[i]
            fa = f * a 
            ga = g * a
            
            f = max(fa, ga, a)
            g = min(fa, ga, a)
            
            res = max(f, res)
            
        return res 
            