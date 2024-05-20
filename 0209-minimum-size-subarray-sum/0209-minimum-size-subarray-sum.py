class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        
        left = 0
        right = 0
        n = len(nums)
        curr_sum = 0
        min_len = n + 1
        
        while right < n:
            curr_sum += nums[right]
            
            while curr_sum >= target:
                min_len = min(min_len, right - left + 1)
                curr_sum -= nums[left]
                left += 1
            right += 1
        return min_len if min_len != n + 1 else 0 
        
        
        
        
            