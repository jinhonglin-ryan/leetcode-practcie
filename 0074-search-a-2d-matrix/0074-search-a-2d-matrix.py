class Solution(object):
    
    
    
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        left = 0
        right = len(matrix) - 1 
        while left <= right:
            mid = left + (right - left) // 2
            
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                left_2 = 0
                right_2 = len(matrix[mid]) - 1
                
                while left_2 <= right_2:
                    mid_2 = left_2 + (right_2 - left_2) // 2
                    if matrix[mid][mid_2] == target:
                        return True
                    elif matrix[mid][mid_2] < target:
                        left_2 = mid_2 + 1
                        continue
                    else:
                        right_2 = mid_2 - 1
                        continue 
                        
                return False
            elif matrix[mid][0] > target:
                right = mid - 1
                continue
            else:
                left = mid + 1
                continue
        return False 