class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        carry = 1
        digits = [0] + digits
        n = len(digits)
        
        for i in range(n - 1, -1, -1):
            digits[i] += carry
            
            if digits[i] // 10 == 1:
                digits[i] = 0
                carry = 1
            else:
                carry = 0
                
        return digits if digits[0] != 0 else digits[1:]