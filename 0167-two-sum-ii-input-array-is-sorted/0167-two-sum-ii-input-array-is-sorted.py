class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        num_to_idx = {}
        
        for i, num in enumerate(numbers):
            complement = target - num
            
            if complement in num_to_idx:
                return [num_to_idx[complement] + 1, i + 1]
            
            num_to_idx[num] = i
        return []