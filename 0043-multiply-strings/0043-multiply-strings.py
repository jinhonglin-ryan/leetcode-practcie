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
        
        # 按照倒序排一下数字，方便从0开始处理
        for i in range(n - 1, -1, -1):
            n1.append(int(num1[i]))
        
        for i in range(m - 1, -1, -1):
            n2.append(int(num2[i]))
            
        n3 = [0] * (n + m)
        
        # num2的第i位和num1的第j位乘的结果放在n3度i+j位
        for i in range(m):
            for j in range(n):
                n3[i + j] += n1[j] * n2[i]
                
        
        k = len(n3)
        
        # 做进位
        carry = 0
        for i in range(k):
            carry += n3[i]
            n3[i] = carry % 10
            carry = carry // 10
        
        # 目前n3的末尾存的是实际上result的开头，要去leading zeros
        k = len(n3) - 1
        
        # 去掉leading zeros, k在这不能减到0，k如果为0的话，说明ans就是一个0，那么return 0 即可 
        while k > 0 and n3[k] == 0:
            k -= 1
            
        res = ""
        
        # 拼接返回答案
        while k >= 0:
            res += str(n3[k])
            k -= 1
            
        return res 
            