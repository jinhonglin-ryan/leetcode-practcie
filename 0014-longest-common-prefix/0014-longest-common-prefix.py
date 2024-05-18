class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        length = len(strs[0])
        count = len(strs)
        
        for i in range(length):
            c = strs[0][i]
            for j in range(1, count):
                if (len(strs[j]) == i) or (strs[j][i] != c):
                    return strs[0][:i]
        return strs[0]
        