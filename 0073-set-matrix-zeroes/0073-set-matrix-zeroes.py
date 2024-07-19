class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # Method 1. 
        # 用第0行的所有列 和 第0列的所有行 来记录是否有0
        # 用r0 和 c0来记录第0行和第0列需不需要变成0
        n = len(matrix)
        m = len(matrix[0])
        
        c0 = False
        r0 = False
        
        for j in range(m):
            if matrix[0][j] == 0:
                r0 = True
                break
                
        for i in range(n):
            if matrix[i][0] == 0:
                c0 = True
                break
                
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0
        
        for i in range(1, n):
            if matrix[i][0] == 0:
                for j in range(1, m):
                    matrix[i][j] = 0
                    
        for j in range(1, m):
            if matrix[0][j] == 0:
                for i in range(1, n):
                    matrix[i][j] = 0
                    
        if r0:
            for j in range(m):
                matrix[0][j] = 0
                
        if c0:
            for i in range(n):
                matrix[i][0] = 0 
            
        
                
        
#         # Method 2.
#         # 用set记录下需要处理的row和col 避免重复计算
#         cols = set()
#         rows = set()
        
#         n = len(matrix)
#         m = len(matrix[0])
        
#         for i in range(n):
#             for j in range(m):
#                 if matrix[i][j] == 0:
#                     rows.add(i)
#                     cols.add(j)
            
#         while rows:
#             i = rows.pop()
            
#             for j in range(m):
#                 matrix[i][j] = 0
                
#         while cols:
#             j = cols.pop()
            
#             for i in range(n):
#                 matrix[i][j] = 0
                    
        
            
            