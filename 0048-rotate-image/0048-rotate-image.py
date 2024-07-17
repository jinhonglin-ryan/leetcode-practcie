class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        # 旋转90度被拆成
        # 1. 沿着对角线翻转
        # 2. 沿着中轴翻转 
        
        
        n = len(matrix)
        
        # 沿对角线翻转
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
                
        # 沿中轴翻转
        for i in range(n):
            j = 0
            k = n - 1
            while j < k:
                # 交换 matrix[i][j] 和 matrix[i][k]
                matrix[i][j], matrix[i][k] = matrix[i][k], matrix[i][j]
                j += 1
                k -= 1
                
        return matrix
        
                
        