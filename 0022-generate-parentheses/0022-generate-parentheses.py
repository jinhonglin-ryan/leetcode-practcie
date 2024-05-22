class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        # Method 1: 
#         all_combo = []
#         curr_combo = []
        
#         def backtrack(symbol, index):
#             if 2 * n == index:
#                 if symbol == 0:
#                     all_combo.append("".join(curr_combo))
#             else:
#                 if symbol < n:
#                     curr_combo.append('(')
#                     backtrack(symbol + 1, index + 1)
#                     curr_combo.pop()
#                 if symbol > 0: 
#                     curr_combo.append(')')
#                     backtrack(symbol - 1, index + 1)
#                     curr_combo.pop()
#         backtrack(0, 0)
#         return all_combo
    
        # Method 2: 
#         res = []
#         # left: # of ( available to use
#         # right: # of ) available to use
#         # curr_string: current combination of ( and )
        
#         def dfs(left, right, curr_string):
#             # print(curr_string)
#             if left == 0 and right == 0:
#                 res.append(curr_string)
#                 return 
#             if left > 0:
#                 dfs(left - 1, right, curr_string + "(")
#             if right > left:
#                 dfs(left, right - 1, curr_string + ")")
                
#         dfs(n, n, "")
#         return res 

        # Method 3:
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