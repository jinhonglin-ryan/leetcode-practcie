class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        
        # 异或操作：计算不带进位的和。
        # 与操作和左移：计算进位 并将其移到正确的位置。
        # 重复迭代：确保所有位都被正确加上，包括进位部分，直到没有进位为止。
        
        MAX_INT = 0x7FFFFFFF # 32 位有符号整数的最大值，二进制表示为0和31个1 
        MASK = 0xFFFFFFFF # 32 位无符号整数的最大值，二进制全是1 
        
        # 保证a和b都在32位中
        a &= MASK
        b &= MASK
        
        while b != 0:
            carry = ((a & b) << 1) & MASK
            
            a = (a ^ b) & MASK
            
            b = carry 
            
        if a <= MAX_INT:
            return a
        else:
            return ~(a ^ MASK)