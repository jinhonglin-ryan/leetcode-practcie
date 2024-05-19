class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # 固定一个数字，然后用two-pointer来找有没有sum to 0
        
        sorted_num = sorted(nums)
        res = []
        for i in range(len(nums)):
            # if we have already had included all the possible result for that number indexed at i (or i - 1), so skip
            if i > 0 and sorted_num[i] == sorted_num[i - 1]:
                continue
            
            
            num_i = sorted_num[i]
            
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                # we want numbers with distinct indices 
                if left == i:
                    left += 1
                    continue 
                    
                if right == i:
                    right -= 1
                    continue
                    
                num_left = sorted_num[left]
                num_right = sorted_num[right]
                temp_sum = num_left + num_right + num_i
                
                
                if temp_sum == 0:
                    res.append([num_i, num_left, num_right])
                    
                    # need to skip the same numbers
                    while left < right and sorted_num[left] == sorted_num[left + 1]:
                        left += 1
                    while left < right and sorted_num[right] == sorted_num[right - 1]:
                        right -= 1
                        
                    left += 1
                    right -= 1
                
                elif temp_sum > 0:
                    right -= 1
                
                else:
                    left += 1
        return res
            

                