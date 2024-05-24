class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
       
        # Method 1: yxc
        # 两次2分：
        # 第一次二分：找出旋转点的index
        # 第二次二分：找出target
        # 二分的本质就是：一段数组满足一个性质，另一段不满足
        # 第一次二分的时候，从nums[0]到旋转点，满足的性质是都大于等于nums[0]
        # 而另一段不满足
        
        n = len(nums)
        if n == 0:
            return -1
        if n == 1:
            return 0 if nums[0] == target else -1
        
        # 第一次二分：找到旋转点的索引 
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        # 旋转点的索引
        pivot = left
        
        # 第二次二分：根据target值确定搜索区间
        left, right = 0, n - 1
        if target >= nums[pivot] and target <= nums[right]:
            left = pivot
        else:
            right = pivot - 1
        
        # 标准二分查找
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
        
        
#         left = 0
#         right = len(nums) - 1
        
#         while left <= right:
#             mid = left + (right - left) // 2
#             if nums[mid] == target:
#                 return mid
            
#             if nums[mid] >= nums[left]:
#                 if nums[mid] > target and target >= nums[left]:
#                     right = mid - 1
#                 else:
#                     left = mid + 1
#             else:
#                 if nums[mid] < target and target <= nums[right]:
#                     left = mid + 1
#                 else:
#                     right = mid - 1

#         return -1