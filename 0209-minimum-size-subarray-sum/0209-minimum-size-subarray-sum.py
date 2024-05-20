class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        
        """
        滑动窗口
        """
        left = 0 
        right = 0
        curr_sum = 0
        min_len = len(nums) + 1
        
        while right < len(nums):
            curr_sum += nums[right]
            
            # 只要curr_sum >= target, 说明满足题目条件，我们要更新min_len
            # 然后减去left的值，并且右移left更新窗口
            # 直到curr_sum < target，我们右移right, 加入一个新的值到窗口中
            while curr_sum >= target:
                min_len = min(min_len, right - left + 1)
                curr_sum -= nums[left]
                left += 1
            
            right += 1
            
        # 如果没有这个array返回0
        return min_len if min_len != len(nums) + 1 else 0 
        
        
        
        
            