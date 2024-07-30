class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        total = sum(nums)
        left = 0
        
        for i in range(len(nums)):
            right = total - nums[i] - left
            
            if right == left:
                return i
            
            left += nums[i]
        return -1