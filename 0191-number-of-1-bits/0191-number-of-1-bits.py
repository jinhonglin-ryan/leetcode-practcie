class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        count = 0
        
        while n > 0:
            if n & 1 == 1:
                count += 1
            n >>= 1 
            
        return count 