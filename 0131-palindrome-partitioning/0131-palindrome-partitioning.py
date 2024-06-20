class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        
        ans = []
        path = []
        def backtrack(startIndex, path):
            if startIndex == len(s):
                ans.append(path[:])
                return
            
            for i in range(startIndex, len(s)):
                if s[startIndex:i+1] == s[startIndex:i+1][::-1]: # 如果是palindrome
                    path.append(s[startIndex:i+1])
                    backtrack(i+1, path)
                    path.pop()
                    
        backtrack(0, path)
        return ans 
                    
            