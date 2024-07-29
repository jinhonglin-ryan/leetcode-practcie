class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        res = -1
        curr_ones = 0
        curr_zeros = 0
        
        left, right = 0, 0
        
        while right < len(nums):
            char = nums[right]
            
            if char == 1:
                curr_ones += 1 
            else:
                curr_zeros += 1
                
            # 如果 0 的数量超过了 k，意味着我们变换k次也没有办法获得全部是1，因此需要调整左指针缩小窗口
            while curr_zeros > k:
                rm = nums[left]
                if rm == 0:
                    curr_zeros -= 1
                else:
                    curr_ones -= 1
                left += 1
                
            # 更新最大长度: 如果curr_zeros 没有大于k了，说明我们可以通过至多k次flip把0变成1，因此总共的1就是curr_ones + curr_zeros
            res = max(res, curr_ones + curr_zeros)
            right += 1
            
        return res 