class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # Method 1: 用two-sum的方法解
#         num_to_idx = {}
        
#         for i, num in enumerate(numbers):
#             complement = target - num
            
#             if complement in num_to_idx:
#                 return [num_to_idx[complement] + 1, i + 1]
            
#             num_to_idx[num] = i
#         return []
    
    
        # Method 2: 用two pointers
        # 利用好numbers是sorted这一个性质
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            num_1 = numbers[left]
            num_2 = numbers[right]
            
            temp_sum = num_1 + num_2
            
            if temp_sum == target:
                return [left + 1, right + 1]
            # 如果目前的sum小于target，说明左边的数不够大，左边的数往右移再尝试
            elif temp_sum < target:
                left += 1
            # 如果目前的sum大于target，说明右边的数过大，右边的数需要左移再尝试
            else: 
                right -= 1
        
        return []