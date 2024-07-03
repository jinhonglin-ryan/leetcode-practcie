class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        # DFS解法
        wordSet = set(wordDict)
        memo = {}        
        
        def dfs(start):
            if start == len(s):
                return True
            
            if start in memo:
                return memo[start]
            
            for end in range(start + 1, len(s) + 1):
                if s[start: end] in wordSet and dfs(end):
                    memo[start] = True
                    return True
                
            memo[start] = False
            return False
        
        return dfs(0)