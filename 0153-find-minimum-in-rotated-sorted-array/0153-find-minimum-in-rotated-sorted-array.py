class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 二分查找
        # rotate之后我们有的是两段升序的subarray（依旧kind of有序）
        # 观察给的example，当mid的值大于right的值时，我们发现mid到right这一部分肯定有旋转点
        # 那么最小值肯定是在mid右边，所以把left更新为 mid + 1
        # 如果mid值小于等于right, 那么最小值肯定在mid左侧或者mid这个位置，所以将right更新为mid然后继续在这个范围内查找
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
        
        
        
        