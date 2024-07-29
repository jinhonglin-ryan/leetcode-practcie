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
                
            while curr_zeros > k:
                rm = nums[left]
                if rm == 0:
                    curr_zeros -= 1
                else:
                    curr_ones -= 1
                left += 1
                
            res = max(res, curr_ones + curr_zeros)
            right += 1
            
        return res 