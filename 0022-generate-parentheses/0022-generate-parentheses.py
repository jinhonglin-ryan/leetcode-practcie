class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        curr_combo = []
        all_combo = []
        
        def dfs(symbol, index):
            if index == 2 * n:
                if symbol == 0:
                    all_combo.append("".join(curr_combo))
            
            else:
                if symbol < n:
                    curr_combo.append("(")
                    dfs(symbol + 1, index + 1)
                    curr_combo.pop()
                if symbol > 0:
                    curr_combo.append(")")
                    dfs(symbol - 1, index + 1)
                    curr_combo.pop()
        dfs(0, 0)
        return all_combo