class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        n1 = []
        n2 = []
        
        n = len(num1)
        m = len(num2)
        
        for i in range(n - 1, -1, -1):
            n1.append(int(num1[i]))
        
        for i in range(m - 1, -1, -1):
            n2.append(int(num2[i]))
            
        n3 = [0] * (n + m)
        
        for i in range(m):
            for j in range(n):
                n3[i + j] += n1[j] * n2[i]
                
        
        k = len(n3)
        
        carry = 0
        for i in range(k):
            carry += n3[i]
            n3[i] = carry % 10
            carry = carry // 10
            
        k = len(n3) - 1
        
        # 去掉leading zeros, k如果为0的话，说明ans就是一个0，那么return 0 即可 
        while k > 0 and n3[k] == 0:
            k -= 1
            
        res = ""
        
        while k >= 0:
            res += str(n3[k])
            k -= 1
            
        return res 
            