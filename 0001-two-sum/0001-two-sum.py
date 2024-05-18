class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # Method 1: 暴力解法
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if (nums[i] + nums[j]) == target:
        #             return [i, j]
                
        # Method 2: Hash Table
        # map integer to its index
        num_to_index = {}

        # iterate over the array 
        for i, num in enumerate(nums):
            # this is the complement number we need for the two-sum
            complement = target - num
            
            # check if such a complement number existed as a key in our dictionary
            if complement in num_to_index:
                # if yes, return the current index i and the complement number index
                return [num_to_index[complement], i]

            # if not, put the current number and its index to the dictionary
            num_to_index[num] = i

        
        return []