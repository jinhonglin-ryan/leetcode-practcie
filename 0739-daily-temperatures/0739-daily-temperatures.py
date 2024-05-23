class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        
        n = len(temperatures)
        stack = []
        ans = [0] * n
        
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                ans[idx] = i - idx
            stack.append(i)
        return ans 
                