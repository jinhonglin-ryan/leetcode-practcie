class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # Method 1. 优化yxc，DP
        # dp[i] 为 i 的二进制表示里的1的个数 
        # 递推公式: dp[i] = dp[i >> 1] + (i & 1)
        
        # 比如100101 的 1的个数 就是 10010的1的个数 + 最后一位是不是1
        
        dp = [0 for _ in range(n + 1)]
        
        dp[0] = 0
        
        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
            
        return dp 
        
#         # Method 2. 暴力
#         nums = [i for i in range(n + 1)]
        
#         res = [0 for _ in range(n + 1)]
        
#         def getOne(a):
#             count = 0
#             while a > 0:
#                 if a & 1 == 1:
#                     count += 1
#                 a >>= 1
#             return count
        
        
#         for i in range(len(nums)):
#             cnt = getOne(nums[i])
#             res[i] = cnt
            
#         return res
            
            