class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        visited = set()
        
        while True:
            if n in visited:
                return False
            
            visited.add(n)
            
            digits = str(n)
            n = sum(int(digit) ** 2 for digit in digits)
            
            if n == 1:
                return True
        
    
       
        