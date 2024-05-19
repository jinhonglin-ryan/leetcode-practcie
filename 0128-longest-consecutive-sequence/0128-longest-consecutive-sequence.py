class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # 用set()
    
        num_set = set(nums)
        longest_length = 0
        
        for num in nums:
            # if num - 1 is in the set, 
            # then the current num is not the start, skip this iteration
            if (num - 1) in num_set:
                continue
                
            # if num - 1 is not in the set
            # then the current num is the start of the sequence
            if (num - 1) not in num_set:
                current_num = num
                current_length = 1
                
                
                while current_num + 1 in num_set:
                    current_length += 1
                    current_num += 1
            longest_length = max(longest_length, current_length)
        
        return longest_length