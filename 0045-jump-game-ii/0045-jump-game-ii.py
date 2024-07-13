class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 贪心
        # 题目设定一定能跳到最远位置
        # 在覆盖范围内找能跳到的最远index（就是每次在「可跳范围」内选择可以使下一次跳的更远的位置。这样才能获得最少跳跃次数。）
        # 同时记录下当前覆盖范围内，所能走到的最远距离，作为下一次的覆盖范围，count ++
        
        n = len(nums)
        
        if n == 1:
            return 0 
        
        curr_end = 0 # 记录下当前点的覆盖的最远距离
        next_end = 0 # 记录下遍历到的最远距离 
        count = 0 # 记录下用到的最小步骤
        
        # 不需要遍历到最后一个数，
        for i in range(len(nums) - 1):
            next_end = max(next_end, i + nums[i])
            
            if i == curr_end: # 到达当前跳跃范围的结束位置
                count += 1 # 更新步数
                curr_end = next_end # 更新下一次跳跃能到的最远位置
                
                # 早停
                if curr_end >= len(nums) - 1:
                    return count 
            
        return count 
        
                
            