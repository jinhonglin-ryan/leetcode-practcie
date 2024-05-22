class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        parentheses = []            # 存放所有括号组合
        parenthesis = []            # 存放当前括号组合
        def backtrack(symbol, index):
            if n * 2 == index:
                if symbol == 0:
                    parentheses.append("".join(parenthesis))
            else:
                if symbol < n:
                    parenthesis.append('(')
                    backtrack(symbol + 1, index + 1)
                    parenthesis.pop()
                if symbol > 0:
                    parenthesis.append(')')
                    backtrack(symbol - 1, index + 1)
                    parenthesis.pop()
        backtrack(0, 0)
        return parentheses