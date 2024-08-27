class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        # 单调栈
        # 需要找到当前元素右边第一个比他大的元素（维护一个递增的单调栈）和当前元素左边第一个比他大的元素（即栈中下一个元素）
        
        ans = 0
        stack = []
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                mid = stack[-1]
                stack.pop()
                if stack:
                    h = min(height[i], height[stack[-1]]) - height[mid]
                    w = i - stack[-1] - 1 
                    ans += h * w 
                
            stack.append(i)
            
        return ans 