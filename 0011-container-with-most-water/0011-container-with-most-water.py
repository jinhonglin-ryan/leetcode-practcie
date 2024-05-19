class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        left = 0 
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            curr_length = right - left
            curr_height = min(height[left], height[right])
            curr_area = curr_length * curr_height
            max_area = max(curr_area, max_area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -=1
        return max_area