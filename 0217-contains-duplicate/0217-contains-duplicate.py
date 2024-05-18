class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # Method 1: Use Set() to store duplicate elements
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        

        # Method 2: Use Dictionary (each element is mapped to a count) 
        # to store duplicate elements 

        # count = {}

        # for num in nums:
        #     if num in count:
        #         count[num] += 1
        #     else:
        #         count[num] = 1
        
        # for key in count:
        #     if count[key] > 1:
        #         return True
        # return False


