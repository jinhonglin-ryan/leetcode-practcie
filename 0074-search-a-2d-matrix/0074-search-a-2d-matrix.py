class Solution(object):
    
    
    
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def binary_search(nums, target):
            left = 0
            right = len(nums) - 1

            while left <= right: 
                mid = (left + right) // 2

                if nums[mid] == target:
                    return True
                elif nums[mid] > target: 
                    right = mid - 1
                else:
                    left = mid + 1 
            return False
    
        for row in matrix:
            if binary_search(row, target):
                return True
        return False