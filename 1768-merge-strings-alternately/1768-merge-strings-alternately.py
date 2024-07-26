class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        
        len1 = len(word1)
        len2 = len(word2)
        
        x1, x2 = 0, 0
        res = ""
        
        while x1 < len1 and x2 < len2:
            res += word1[x1]
            res += word2[x2]
            
            x1 += 1
            x2 += 1
            
        while x1 < len1:
            res += word1[x1]
            x1 += 1
            
        while x2 < len2:
            res += word2[x2]
            x2 += 1
            
        return res 