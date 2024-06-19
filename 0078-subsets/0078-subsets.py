class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Method 1：backtrack 
        ans = []
        path = []
        def backtrack(nums, index):
            ans.append(path[:])
            if index >= len(nums): return
            
            for i in range(index, len(nums)):
                path.append(nums[i])
                backtrack(nums, i + 1)
                path.pop()
        backtrack(nums, 0)
        return ans
    
    
#         # Method 2：二进制的思想
#         # 由于每个数有选和不选两种情况，因此总共有 2^n 种情况，用二进制 0 到 2^n 表示所有的情况，在某种情况i中，若该二进制i的第j位是1，则表示第j位这个数选，加入到path中，枚举完i这种情况，将path加入到ans链表中
#         # 枚举0到2^n - 1个数，其中每一位代表该数选或不选
#         # 比如[1，2，3] 这个集合, 我们就是会枚举出8种情况，000，001，010，100，110，101，011，111这8种 分别对应了0-2^n -1 这些数的2进制表示
#         # 如果当前数为0，则对应的集合中的数不选
#         # 如果当前数为1，则对应的集合中的数选
#         # 时间复杂度: n*2^n 
#         # 实现：
#         res = []
#         n = len(nums)
#         for i in range(0, 2 ** n): # i是0-2^n-1 所有数的二进制表示
#             path = []
#             # 对于一个i（表示一个二进制），我们考虑每个数是否选择的情况，j表示了当前数字是否要选，j从0到n-1，比如n=3，我们就考虑这三个数中的每一个数字是否要选
#             for j in range(n):
#                 # 如果i向右移动j位后与1 and 是1：代表i的二进制表示中第 j 位是1，所以我们将nums[j]加入path中
#                 # 比如i=5，二进制表示是101，那么代表了nums的第一个数和第三个数是要选的，因为i的二进制在第一个数和第三个数的位置为1
#                 if (i >> j) & 1:
#                     path.append(nums[j])
            
#             res.append(path)
            
#         return res
            
        
        