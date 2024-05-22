class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Method 1: Recursive binary search
#         def binary_search(left, right):
#             if left > right:
#                 return -1 
            
#             mid = (left + right) // 2
            
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] > target:
#                 return binary_search(left, mid - 1)
#             else:
#                 return binary_search(mid + 1, right)
        
#         return binary_search(0, len(nums) - 1)
    
        # Method 2: Iterative Binary Search
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
                continue
            else: 
                left = mid + 1
                continue
        return -1