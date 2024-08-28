class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        # 单调栈
        # 思路：维护一个单调递减栈，即从栈头到栈尾是递减的
        # 遍历每一个柱子，找到左边第一个比他矮的柱子（即栈的下一个元素），和右边第一个比他矮的柱子（单调栈）
        # 细节：首尾+一个0保证原先的第一个元素和最后一个元素可以找到左边/右边第一个比他小的元素
        
        ans = 0
        
        stack = []
        
        h = [0] * (len(heights) + 2)
        
        j = 0
        
        for i in range(1, len(h) - 1):
            h[i] = heights[j]
            j += 1 
            
        
        for i in range(len(h)):
            while stack and h[i] < h[stack[-1]]:
                mid = stack.pop()
                if stack:
                    left = stack[-1]
                    right = i
                    w = right - left - 1
                    height = h[mid]
                    ans = max(ans, w * height)
                                    
            stack.append(i)
                    
        return ans 
                    
                    
                