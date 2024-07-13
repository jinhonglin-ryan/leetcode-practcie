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
        
        # 删除相邻的重复元素
        new_nums = [nums[0]]
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                new_nums.append(nums[i])
        
        if len(new_nums) == 1:
            return 1
        
        res = 2
        for i in range(1, len(new_nums) - 1):
            a = new_nums[i - 1]
            b = new_nums[i]
            c = new_nums[i + 1]
            if (b > a and b > c) or (b < a and b < c):
                res += 1
                
        return res
            
        
        
        