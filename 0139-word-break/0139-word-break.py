class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
#         # Method 1. DFS解法
#         # 深度优先搜索（DFS）和记忆化（memoization）
#         wordSet = set(wordDict)
#         memo = {}        
        
#         def dfs(start):
#             if start == len(s):
#                 return True
            
#             if start in memo:
#                 return memo[start]
            
#             for end in range(start + 1, len(s) + 1):
#                 if s[start: end] in wordSet and dfs(end):
#                     memo[start] = True
#                     return True
                
#             memo[start] = False
#             return False
        
#         return dfs(0)
    
    
        # Method 2. 常规DP解法
        # dp[i] 表示前i个字符可不可以被拆分成dict里的
        # 返回dp[n]
        
        n = len(s)
        
        dp = [False for _ in range(n + 1)]
        
        dp[0] = True
        
        # 外层循环表示字串的结束位置
        for i in range(1, n + 1):
            for j in range(i): # 内层循环表示字串的起始位置
                if s[j: i] in wordDict and dp[j]:
                    dp[i] = True
                    
        return dp[n]