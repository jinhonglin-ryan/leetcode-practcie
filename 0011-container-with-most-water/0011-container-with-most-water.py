class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        """
        双指针：分别从最左边和从最右边开始向中心移动，每次算一次当前面积，与max面积比较，然后舍弃掉较短的一边，移动短边的指针，试图获得更高的高度从而获得更大的面积
        """
        
        left = 0 
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            curr_length = right - left
            # 高度取决于短的那条bar
            curr_height = min(height[left], height[right])
            curr_area = curr_length * curr_height
            max_area = max(curr_area, max_area)
            
            # 尝试找到更大的面积
            # 如果left的height更小，我们想要left++来尝试找到一个更高的height，这样可能会给我们一个更大的面积，如果right的height更小，同理
            # 为什么不移动height更大的那个指针：因为height更大是我们想要保留的，如果移动了之后，面积可能会变小
            # 每次都算一遍当前的面积并且更新(if needed) max_area
            if height[left] < height[right]:
                left += 1
            else:
                right -=1
        return max_area