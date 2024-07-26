class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        l = 0  # 用来标记下一个非零元素的位置

        # 遍历数组
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l] = nums[r]
                l += 1

        # 将 l 之后的所有元素置为零
        for i in range(l, len(nums)):
            nums[i] = 0

        return nums

                
                
                    