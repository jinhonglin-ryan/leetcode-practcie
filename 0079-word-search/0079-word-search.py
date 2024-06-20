class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # m表示了board有几行
        # n表示了board有几列
        m = len(board)
        n = len(board[0])
        
        # i, j 表示board上的index
        # k表示word的index
        def backtrack(i, j, k):
            # 如果越界，或者board上的字符跟word上的当前字符不匹配，return False
            if not 0 <= i < m or not 0 <= j < n or board[i][j] != word[k]:
                return False
            elif k == len(word) - 1: # 隐含条件：上一层if没有进去，说明没有越界，并且字符匹配，且我们走到了word的最后一个字符
                return True
            else: # # 隐含条件：第一层if没有进去：没有越界，并且字符匹配，但是还没走到word的最后一个字符
                # 修改board当前的字符 表示字符被用过 
                board[i][j] = ''
                # 尝试走四个方向
                res = backtrack(i+1, j, k+1) or backtrack(i-1, j, k+1) or backtrack(i, j+1, k+1) or backtrack(i, j-1, k+1)
                # 恢复现场
                board[i][j] = word[k]
                return res
        
        # 爆搜，对每个board中的每个点都当作起点，去找有没有和word匹配的string
        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
                
        return False 
        
                
                
        