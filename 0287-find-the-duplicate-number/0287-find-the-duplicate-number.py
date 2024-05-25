class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count = {}
        for num in nums:
            if num in count:
                return num
            count[num] = 1
        return 