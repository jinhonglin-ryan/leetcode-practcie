class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
                
        if len(str2) == 0:
            return str1
        
        # 使得str1为较长的字符串
        if len(str2) > len(str1):
            str1, str2 = str2, str1
        
        # 把str2从str1中减去
        l1 = len(str1)
        l2 = len(str2)
        
        for i in range(l2):
            if str1[i] != str2[i]:
                return ""

        return self.gcdOfStrings(str1[l2:], str2)

        
        
        
        
        
        