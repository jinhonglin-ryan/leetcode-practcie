class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        # 在一次遍历中 检查 每一行 每一列 和每一个sub box
        # 用set()
        # 9列，9行，9个subbox: 每一列，每一行，和每一个subbox 都应该有一个set来记录  
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]
        
        # i 来记录rows: 所以rows[i] 代表第i行的set
        # j 来记录cols: 所以cols[j] 代表第j行的set
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue 
                
                # 这个num在第i行的set里重复了，return False
                if num in rows[i]:
                    return False
                else: # else的话正常加入set
                    rows[i].add(num)
                
                # 与上同理
                if num in cols[j]:
                    return False
                else:
                    cols[j].add(num)
                    
                
                # 算subbox index 定义subbox index如下
                # 其余逻辑与上同理 
                """
                +-------+-------+-------+
                |   0   |   1   |   2   |
                |       |       |       |
                +-------+-------+-------+
                |   3   |   4   |   5   |
                |       |       |       |
                +-------+-------+-------+
                |   6   |   7   |   8   |
                |       |       |       |
                +-------+-------+-------+
                """
                subbox_index = (i // 3) * 3 + (j // 3)
                
                if num in squares[subbox_index]:
                    return False
                else:
                    squares[subbox_index].add(num)
        return True