class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        cols = set()
        rows = set()
        
        
        
        n = len(matrix)
        m = len(matrix[0])
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
            
        while rows:
            i = rows.pop()
            
            for j in range(m):
                matrix[i][j] = 0
                
        while cols:
            j = cols.pop()
            
            for i in range(n):
                matrix[i][j] = 0
                    
        
            
            