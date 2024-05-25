class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        # Method 1: 不满足要求，空间复杂度是O(n)
        # count = {}
        # for num in nums:
        #     if num in count:
        #         return num
        #     count[num] = 1
        # return -1 
    
    
        # Method 2: 二分
        # [left, right] 初始化表示 [1, n] 这个区间
        # 取这个区间的中间值
        # 比如我们的n是5，[1, 2, 3, 4, 5] 中间值就是3
        # 我们将[1, n]这个区间分成了[left, mid] 和 [mid + 1, right] 
        # 一开始的时候 left = 1, right = n
        # 然后遍历nums， 记录小于等于中间值的count
        # 在一个没有重复的数组中，[1, mid] 中小于等于mid的数应该有mid个
        # 但是如果有重复的情况的话，就需要分类讨论
        # 如果count <= mid:
    
        # 那么
        
        left = 1
        right = len(nums) - 1 # n + 1 - 1 = n
        
        
        while left < right:
            mid = left + (right - left) // 2
            
            count = 0
            
            for num in nums:
                if num <= mid:
                    count += 1
                    
            if count <= mid:
                left = mid + 1 
            else:
                right = mid
        
        return left 
        