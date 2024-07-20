class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        nums = sorted(nums)
        
        for i in range(n):
            if nums[i] != i:
                return i
            
        return i + 1