class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        nums = sorted(nums)
        
        l, r = 0, len(nums) - 1
        cnt = 0
        
        while l < r:
            curr_sum = nums[l] + nums[r]
            
            if curr_sum == k:
                l += 1
                r -= 1
                cnt += 1
            
            elif curr_sum > k:
                r -= 1
                
            else:
                l += 1
                
        return cnt 