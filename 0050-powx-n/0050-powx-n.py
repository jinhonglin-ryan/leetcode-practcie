class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        # 快速幂算法
        # 把指数拆成二进制
        
        is_minus = n < 0 
        res = 1.0 
        # 先考虑指数的绝对值
        n = abs(n)
        
        while n > 0:
            # 如果 n 的最低位（最右边的位）是 1
            if n & 1:
                res *= x
            # 累加x
            x *= x
            # n 的二进制表示右移一位
            n >>= 1
            
        if is_minus:
            res = 1 / res
            
        return res 
            
            
                
        
        