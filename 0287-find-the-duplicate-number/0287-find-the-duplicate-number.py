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
        # 取这个区间的中间值 n + 1 // 2
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
        