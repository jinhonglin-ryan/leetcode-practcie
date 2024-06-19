class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Method 1：backtrack 
#         def backtrack(start, path):
#         # 添加当前子集到结果中
#             res.append(path[:])  # 使用path[:]来避免引用问题
#             # 从start开始，尝试包含更多的元素
#             for i in range(start, len(nums)):
#                 # 添加当前元素到路径
#                 path.append(nums[i])
#                 # 递归，移动到下一个元素
#                 backtrack(i + 1, path)
#                 # 回溯，移除路径中的最后一个元素
#                 path.pop()
    
#         res = []
#         backtrack(0, [])
#         return res
    
    
        # Method 2：二进制的思想
        # 枚举0到2^n - 1个数，其中每一位代表该数选或不选
        # 比如[1，2，3] 这个集合, 我们就是会枚举出8种情况，000，001，010，100，110，101，011，111这8种 分别对应了0-2^n -1 这些数的2进制表示
        # 如果当前数为0，则对应的集合中的数不选
        # 如果当前数为1，则对应的集合中的数选
        # 时间复杂度: n*2^n 
        # 实现：
        res = []
        n = len(nums)
        for i in range(0, 2 ** n): # i是0-2^n-1 所有数的二进制表示
            path = []
            # 对于一个i（表示一个二进制），我们考虑从0到i-1个j的情况，比如现在i=5，二进制表示是101
            # j是从0到4 inclusive
            for j in range(0, n):
                if (i >> j) & 1:
                    path.append(nums[j])
            
            res.append(path)
            
        return res
            
        
        