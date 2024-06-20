class Solution(object):
    
    def __init__(self):
        self.result = []

    def restoreIpAddresses(self, s):
        self.backtracking(s, 0, 0)
        return self.result

    def backtracking(self, s, startIndex, pointNum):
        if pointNum == 3:
            if self.isValid(s, startIndex, len(s) - 1):
                self.result.append(s)
            return
        
        for i in range(startIndex, len(s)):
            if self.isValid(s, startIndex, i):
                s = s[:i+1] + '.' + s[i+1:]  # 在 i 后面插入点
                pointNum += 1
                self.backtracking(s, i + 2, pointNum)  # 移至下一个子串的起始位置
                pointNum -= 1
                s = s[:i+1] + s[i+2:]  # 移除插入的点
            else:
                break  # 当前子串不合法时终止循环

    def isValid(self, s, start, end):
        if start > end:
            return False
        if s[start] == '0' and start != end:  # 排除多位数以0开头的情况
            return False
        num = 0
        for i in range(start, end + 1):
            if not s[i].isdigit():  # 非数字字符
                return False
            num = num * 10 + int(s[i])
            if num > 255:
                return False
        return True