class Solution(object):
    
    
    
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Method 1: My solution
        # 一行一行分别binary search 
#         def binary_search(nums, left, right):
#             if left > right:
#                 return False
            
#             mid = (left + right) // 2
            
#             if nums[mid] == target:
#                 return True
#             elif nums[mid] > target:
#                 return binary_search(nums, left, mid - 1)
#             else:
#                 return binary_search(nums, mid + 1, right)
        
#         for row in matrix:
#             if binary_search(row, 0, len(row) - 1):
#                 return True
                
#         return False
        
        # Method 2: 先使用二分查找确定目标值所在的行，然后在该行内再次使用二分查找确定目标值所在的列
        left = 0
        right = len(matrix) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                left_2 = 0
                right_2 = len(matrix[0]) - 1 
                
                while left_2 <= right_2:
                    mid_2 = left_2 + (right_2 - left_2) // 2
                    
                    if matrix[mid][mid_2] == target:
                        return True
                    elif matrix[mid][mid_2] > target:
                        right_2 = mid_2 - 1
                        continue
                    else:
                        left_2 = mid_2 + 1 
                        continue
                return False
                        
            elif matrix[mid][0] > target:
                right = mid - 1
                continue
            else:
                left = mid + 1
                continue
        return False
        
        
        