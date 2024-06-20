class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        
        digit_to_letter = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        
        ans = []
        path = ""
        # index 表示 当前走到 digits的哪一个位置了
        def backtrack(path, index):
            if index == len(digits): # 如果当前走到了digits的末尾的后一个位置（等价于path中有len(digits)个数字，我们把path 加入ans）
                ans.append(path)
            else: # 如果还没走到digits的末尾
                digit = digits[index]
                letter = digit_to_letter[digit]
                for i in range(0, len(letter)):
                    path += letter[i]
                    backtrack(path, index + 1)
                    path = path[0:len(path) - 1]
                    
        backtrack(path, 0)
        return ans 
                
        