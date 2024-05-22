class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
#         ans = []
#         def dfs(lc, rc, n, curr):
#             if lc == 0 and rc == 0:
#                 ans.append(curr)
#             else: 
#                 if lc < n:
#                     dfs(lc + 1, rc, n, curr + "(")
#                 if rc < n and lc > rc:
#                     dfs(lc, rc + 1, n, curr + ")")
        
#         dfs(0, 0, n, "")
#         return ans 
                
        ans = []
        
        def dfs(lc, rc, n, curr_string):
            if lc == n and rc == n:
                ans.append(curr_string)
            else:
                if lc < n:
                    dfs(lc + 1, rc, n, curr_string + "(")
                if rc < n and lc > rc:
                    dfs(lc, rc + 1, n, curr_string + ")")
        dfs(0, 0, n, "")       
        return ans