class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # 遍历nums数组，记录能跳到的最远位置
        max_reach = 0
        for i in range(len(nums)):
            if max_reach < i :
                return False
            
            max_reach = max(max_reach, i + nums[i])
            
        return True 