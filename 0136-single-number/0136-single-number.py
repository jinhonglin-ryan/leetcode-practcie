class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # 异或运算
        # 1. 交换率 和 结合率 
        # 2. x ^ x = 0
        # 3. a ^ 0 = a
        
        n = len(nums)
        if n == 1:
            return nums[0]
        
        res = 0
        
        for num in nums:
            res ^= num
            
        return res 
            
        