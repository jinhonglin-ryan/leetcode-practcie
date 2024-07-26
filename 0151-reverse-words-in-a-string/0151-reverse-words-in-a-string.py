class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        slist = s.split()
        # slist = list(" ".join(words))
        
        res = ""
        
        for i in range(len(slist) - 1, -1, -1):
            res += slist[i]
            res += " "
        
        res = res.strip()
        
        return res 