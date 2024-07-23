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
        
        # 获得 a和b的lower 32 bits，把a和b看作32位无符号整数，最后对a的范围进行判断，返回成 有符号整数
        a &= MASK
        b &= MASK
        
        # 当 b 不为 0 时，表示还有进位需要处理。
        while b != 0:
            # 计算进位，并将进位左移一位，同时使用 MASK 限制在 32 位内。
            carry = ((a & b) << 1) & MASK
            
            # 计算不带进位的和，确保在32位内
            a = (a ^ b) & MASK
            
            b = carry 
        
       
        # a是一个非负数，直接返回 a。
        if a <= MAX_INT:
            return a
        # 当 a 超过32位有符号整数的最大值时，溢出，返回对应的负数
        else:
            return ~(a ^ MASK)