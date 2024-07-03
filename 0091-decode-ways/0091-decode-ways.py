class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # DP
        # 1. 状态表示
        # dp[i] 表示的集合是 所有由前i个字符 可以解码回去的形成的字符串的集合
        # 比如 126 可以解码回 AZ 和 ABF，那么 dp[3] 就表示这个AZ和ABF的集合 属性为这个集合里的个数 
        # dp[i] 表示s 前 i 个字符构成的字符串可能构成的翻译方案数。
        # 所以需要返回dp[n]
        
        # 2. 状态计算
        # dp[i] 可以被分解为 最后一个字符对应了一个数字，所以方案数就是dp[i] += dp[i - 1]
        # 也可以是最后一个字符对应的是两个数字, 所以方案数就是dp[i] += dp[i - 2]
        
        # 比如s = 12 dp[1] = 1 即1只有一种解码方式
        # dp[2] 是在看12有几种解码方式，dp[2] 一开始是0，可以把2看成一个字符，所以dp[2] += dp[1] = 1, 也可以把12看成一个字符，所以dp[2] += dp[0] (dp[0]是1) = 2
        # 所以12一共有两种解码方式
        
        n = len(s)
        
        if n == 1:
            if s[0] == '0':
                return 0
            else:
                return 1
            
        dp = [0 for _ in range(n + 1)]
        
        dp[0] = 1
        
        if s[0] == '0':
            return 0
        
        for i in range(1, n + 1):
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            
            if i > 1 and s[i - 2] != '0' and int(s[i - 2: i]) <= 26:
                dp[i] += dp[i - 2]
                
        return dp[n]
            