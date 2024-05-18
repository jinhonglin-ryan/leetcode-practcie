class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        # 以第一个str作为基准
#         length = len(strs[0])
#         count = len(strs)
        
#         for i in range(length):
#             c = strs[0][i]
            
#             for j in range(1, count):
#                 if (len(strs[j]) == i) or (strs[j][i] != c):
#                     return strs[0][:i]
#         return strs[0]
        prefix = strs[0]

        # 依次比较每个字符串
        for s in strs[1:]:
            # 缩短前缀直到找到匹配的前缀
            while s.find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix
        