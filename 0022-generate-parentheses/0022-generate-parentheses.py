class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
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
    
    
        res = []
        
        def dfs(left, right, curr_string):
            if left == 0 and right == 0:
                res.append(curr_string)
                return 
            if left > 0:
                dfs(left - 1, right, curr_string + "(")
            if right > left:
                dfs(left, right - 1, curr_string + ")")
                
        dfs(n, n, "")
        return res 