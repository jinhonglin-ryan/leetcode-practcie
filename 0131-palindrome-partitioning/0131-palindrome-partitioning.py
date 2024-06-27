class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        
        # 子集型 backtrack回溯
        # 枚举aab之间的两个逗号，是选/不选
         
        ans = []
        path = []
        def backtrack(startIndex, path):
            if startIndex == len(s): # 如果startIndex走到末尾了，将path加入ans
                ans.append(path[:])
                return
            # i表示在哪里分割，startIndex表示起点
            # check从startIndex到i这一段，如果是palindrome，把这个作为path的一个元素，加入path
            # 然后check 从第i个位置的下一个位置开始，在哪里分割可以得到palindrome
            for i in range(startIndex, len(s)):
                if s[startIndex:i+1] == s[startIndex:i+1][::-1]: # 如果从startIndex到i这一段是palindrome
                    path.append(s[startIndex:i+1]) # 则将这一段内容加入path
                    backtrack(i+1, path) # 然后在i+1个位置开始往后面找palindrome
                    path.pop() # 恢复path 
                    
        backtrack(0, path)
        return ans 