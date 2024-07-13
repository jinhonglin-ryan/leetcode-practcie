class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        # 处理trivial 情况
        if n == 1:
            return 1
        
        if n == 2:
            return 2 if nums[0] != nums[1] else 1
        
        # 默认数组最右边有一个摆动
        res = 1
        # 相当于在起点前延伸一个pre_diff
        pre_diff = 0
        
        for i in range(n - 1):
            next_diff = nums[i + 1] - nums[i]
            
            if (pre_diff >= 0 and next_diff < 0) or (pre_diff <= 0 and next_diff > 0):
                res += 1 
                pre_diff = next_diff
                
        return res
            
        
        
        