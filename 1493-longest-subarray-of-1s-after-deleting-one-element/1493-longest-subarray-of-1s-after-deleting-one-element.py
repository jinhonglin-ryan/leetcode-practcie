class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Sliding window
        # 维护一个window，其中0的数量<=1 
        
        res = -1
        curr_ones = 0
        curr_zeros = 0 
        
        
        left, right = 0, 0
        
        while right < len(nums):
            now = nums[right]
            
            if now == 1:
                curr_ones += 1
            else:
                curr_zeros += 1
        
            while curr_zeros > 1:
                first = nums[left]
                if first == 1:
                    curr_ones -= 1
                else:
                    curr_zeros -= 1
                left += 1
            
            
            res = max(res, curr_ones)
                
            right += 1
        
        if res == len(nums):
            return res - 1
        
        return res 
            