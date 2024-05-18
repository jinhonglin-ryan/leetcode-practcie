class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        # 以第一个str作为基准
        length = len(strs[0])
        count = len(strs)
        
        # 遍历第一个string by character
        for i in range(length):
            c = strs[0][i]
            
            # 对于第i-th character，遍历strs中的其他string，比较在i这个位置的character
            # 是否和c一样
            for j in range(1, count):
                # 如果当前string的长度就是i的长度，遍历结束
                # 或者 如果当前string第i个位置的character 跟c不一样 遍历结束
                if (len(strs[j]) == i) or (strs[j][i] != c):
                    # 返回第一个string的前i个character作为longest common prefix
                    return strs[0][:i]
        # code执行到这 说明一直没有退出，则整个first string是longest common prefix
        return strs[0]
        