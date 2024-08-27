class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        # Method 1 用单调栈做
        # 本质上是找到当前元素右边的最大元素
        # 求一个元素右边第一个更大元素，单调栈就是递增的：递增为从栈头到栈底是递增的
        # 栈中存索引
        
        n = len(temperatures)
        ans = [0 for _ in range(n)]
        stack = []
        
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                ans[index] = i - index
            stack.append(i)
        
        return ans
    
        # Method 2 暴力解法（超时）
#         n = len(temperatures)
#         count = {i: 0 for i in range(n)}
#         ans = [0] * n

#         for i in range(n):
#             for j in range(i + 1, n):
#                 if temperatures[j] > temperatures[i]:
#                     count[i] = j - i
#                     break
#         for i in range(n):
#             ans[i] = count[i]

#         return ans
                