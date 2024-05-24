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
            mid = (left + right + 1) // 2
            if nums[mid] >= nums[0]:
                left = mid
            else:
                right = mid - 1
                
        # 在上面这个二分后 旋转点的index确定了，就是left = right 
        # 如果target 大于等于nums[0]的值，我们在0到旋转点这里找target
        # else 我们在0到旋转点+1到len(nums) - 1找
        # 旋转点的索引
        
        if target >= nums[0]:
            left = 0
        else:
            left = right + 1
            right = n - 1
        
        # 第二次二分：根据上面确定的left与right找target
        # 标准二分查找
        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1 
                
        if nums[right] == target:
            return right
        
        return -1
        
        # Method 2
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