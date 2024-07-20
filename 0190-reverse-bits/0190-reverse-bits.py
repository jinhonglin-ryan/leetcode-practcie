class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        
        for i in range(32):
            # 获取 n 的最低位
            bit = n & 1
            
            # 将 bit 移到对应的位置，并累加到 result
            res = (res << 1) | bit
            
            # 右移 n，处理下一位
            n >>= 1
            
        return res 
        