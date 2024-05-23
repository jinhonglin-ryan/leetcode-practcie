class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        # 用一个栈来保存未找到比它们更高温度的那些天的索引
        # 栈中的索引对应的实际温度是单调递减的，这样可以确保每次遇到一个更高温度时，可以一次性处理掉栈中所有较低温度的天数。
        # 单调递减，为什么？如果当前温度 temperatures[i] 小于或等于栈顶索引对应的温度 temperatures[stack[-1]]，我们直接将当前索引 i 压入栈中。这样保持了栈中温度的单调递减性。
        # 当我们遇到一个更高的温度 temperatures[i] 时，我们需要处理栈中所有比当前温度低的温度。这时，我们会弹出栈顶元素，并更新这些温度对应的等待天数。
        

        n = len(temperatures)
        ans = [0 for _ in range(n)]
        stack = []
        
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                ans[index] = i - index
            stack.append(i)
        return ans
                