class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        # 在0-x的范围遍历，找到k^2 <= x的最大值
        
        left = 0
        right = x
        
        while left < right:
            mid = left + (right - left) // 2 + 1
            
            if mid * mid <= x:
                left = mid
            else:
                right = mid - 1
                
        return left 
                