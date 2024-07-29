class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        left, right = 0, 0
        max_sum = -float('inf')
        curr_sum = 0
        
        while right < k:
            curr_sum += nums[right]
            right += 1
            
        max_sum = max(max_sum, curr_sum)
        
        while right < len(nums):
            curr_sum += nums[right]
            right += 1
            curr_sum -= nums[left]
            left += 1
            max_sum = max(max_sum, curr_sum)
            
        return float(max_sum) / k
        
                    