class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 贪心
        # 题目设定一定能跳到最远位置
        # 在覆盖范围内找能跳到的最远index
        # 
        
        n = len(nums)
        
        if n == 1:
            return 0 
        
        curr_end = 0 # 记录下当前点的覆盖的最远距离
        max_end = 0 # 记录下遍历到的最远距离 
        count = 0 # 记录下用到的最小步骤
        
        for i in range(len(nums) - 1):
            max_end = max(max_end, i + nums[i])
            
            if i == curr_end:
                count += 1 
                curr_end = max_end
            
        return count 
        
                
            