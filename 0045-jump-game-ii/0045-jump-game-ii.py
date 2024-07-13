class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 贪心
        # 一定能跳到最远位置
        # 在覆盖范围内找能跳到的最远index
        
        n = len(nums)
        
        if n == 1:
            return 0 
        
        end, max_pos = 0, 0
        steps = 0
        for i in range(len(nums) - 1):
            max_pos = max(max_pos, nums[i] + i)
            if i == end:
                end = max_pos
                steps += 1
        return steps
                
            