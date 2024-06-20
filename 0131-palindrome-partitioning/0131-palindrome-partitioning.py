class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        
        ans = []
        path = []
        def backtrack(startIndex, path):
            if startIndex == len(s): # 如果startIndex走到末尾了，将path加入ans
                ans.append(path[:])
                return
            
            for i in range(startIndex, len(s)):
                if s[startIndex:i+1] == s[startIndex:i+1][::-1]: # 如果是palindrome
                    path.append(s[startIndex:i+1]) # 则将这一段内容加入path
                    backtrack(i+1, path) # 然后在i+1个位置开始往后面找palindrome
                    path.pop() # 恢复path 
                    
        backtrack(0, path)
        return ans 
                    
            