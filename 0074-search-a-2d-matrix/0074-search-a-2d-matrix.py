class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        def binary_search(nums, left, right):
            if left > right:
                return False
            
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                return binary_search(nums, left, mid - 1)
            else:
                return binary_search(nums, mid + 1, right)
        
        for row in matrix:
            if binary_search(row, 0, len(row) - 1):
                return True
                
        return False

            