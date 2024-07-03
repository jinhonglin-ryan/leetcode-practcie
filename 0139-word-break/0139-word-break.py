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
    
    
#         # Method 2. 常规DP解法
#         # dp[i] 表示前i个字符可不可以被拆分成dict里的
#         # 返回dp[n]
        
#         n = len(s)
        
#         dp = [False for _ in range(n + 1)]
        
#         dp[0] = True
        
#         # 外层循环变量 i 从 1 遍历到 n，表示当前考虑的子字符串的结束位置。
#         # 每次循环开始，i 表示我们正在检查前 i 个字符（即 s[0:i]）是否可以被拆分成字典中的单词。
#         for i in range(1, n + 1):
#             # 内层循环变量 j 从 0 遍历到 i-1，表示当前考虑的子字符串的开始位置。
#             for j in range(i): 
#                 if s[j: i] in wordDict and dp[j]:
#                     dp[i] = True
                    
#         return dp[n]

        # Method 3. 区间DP解法 （不推荐）
        # dp[i][j] 表示s在i,j inclusive index 区间可不可以被拆分成wordDict里的词
        # 返回dp[0][n - 1]
        
        n = len(s)
        
        dp = [[False for _ in range(n)] for _ in range(n)]
        
        # 区间dp枚举方法
        # 外层枚举区间长度
        for length in range(1, n + 1):
            # 内层枚举起始位置
            for i in range(n - length + 1):
                j = length + i - 1 # 终点位置
                
                if s[i: j + 1] in wordDict:
                    dp[i][j] = True
                else:
                    for k in range(i, j):
                        if dp[i][k] and dp[k + 1][j]:
                            dp[i][j] = True
                            break
                            
                            
        return dp[0][n - 1]

        