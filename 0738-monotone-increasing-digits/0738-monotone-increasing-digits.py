class Solution(object):
    def monotoneIncreasingDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # 贪心的思想
        # 从后往前遍历，如果前一位可以-1，就做-1，然后后一位变成9
        # 比如 332，先变成329，再变成299
        # 需要记录一个 spot where the digit at and after this spot will be made to 9
        # Python 的字符串是不可变的，无法直接通过索引修改字符串的某个字符
        # 因此用list
        
        
        nlist = list(str(n))
        
        # 如果真是全部递增，那就不需要变spot
        spot = len(nlist)
        
        for i in range(len(nlist) - 1, 0, -1):
            if nlist[i - 1] > nlist[i]:
                nlist[i - 1] = str(int(nlist[i - 1]) - 1)
                spot = i
                
        for i in range(spot, len(nlist)):
            nlist[i] = '9'
        
        
        return int("".join(nlist))
        
            