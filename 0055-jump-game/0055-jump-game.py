class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # 遍历nums数组，记录能跳到的最远下标
        max_reach = 0
        
        for i in range(len(nums)):
            # i是会到len(nums) - 1 这个最远下标的
            if max_reach < i :
                return False
            
            max_reach = max(max_reach, i + nums[i])
            
            # 早停
            if max_reach == len(nums) - 1:
                return True
            
        return True 