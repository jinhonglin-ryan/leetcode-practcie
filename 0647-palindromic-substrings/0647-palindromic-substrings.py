class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 同第五题的dp解法
        # 只需要最后遍历一下dp数组，数一下有多少True的项
        
        n = len(s)
        if n == 0:
            return 0
        
        if n == 1:
            return 1
        
        dp = [[False for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = True
        
        # 区间dp的循环写法：
        # 外层枚举长度，内层枚举左端点
        for length in range(1, n + 1):  # 子串长度从 1 到 n
            for i in range(n - length + 1): # 枚举左端点位置
                
                j = i + length - 1  # 子串结束位置

                if s[i] == s[j]:
                    if j - i <= 2:  # 长度为1, 2, 3的子串, 只需验证两个字符是否相等
                        dp[i][j] = True
                        
                    else:  # 长度大于2的子串, 需要验证去掉首尾后的子串是否回文
                        dp[i][j] = dp[i + 1][j - 1]
        
        count = 0
        for i in range(n):
            for j in range(n):
                if dp[i][j]:
                    count += 1
                    
        return count 