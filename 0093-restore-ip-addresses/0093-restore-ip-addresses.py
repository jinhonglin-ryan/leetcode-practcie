class Solution(object):
    
    def __init__(self):
        self.result = []

    def restoreIpAddresses(self, s):
        self.backtracking(s, 0, 0)
        return self.result

    def backtracking(self, s, startIndex, pointNum):
        if pointNum == 3: # 每次插入一个点之后 check
            if self.isValid(s, startIndex, len(s) - 1):
                self.result.append(s)
            return
        
        for i in range(startIndex, len(s)):
            if self.isValid(s, startIndex, i):
                s = s[:i+1] + '.' + s[i+1:]  # 在 i 后面插入点
                pointNum += 1
                self.backtracking(s, i + 2, pointNum)  # 移至下一个子串的起始位置， i+2 因为要跳过刚加入的点.
                pointNum -= 1
                s = s[:i+1] + s[i+2:]  # 移除插入的点
            else:
                break  # 当前子串不合法时终止循环

    def isValid(self, s, start, end): # 左闭 右闭区间
        if start > end:
            return False
        
        if s[start] == '0' and start != end:  # 排除多位数以0开头的情况
            return False
        
        curr = s[start:end+1]
        if not 0 <= int(curr) <= 255: # 如果curr的数字不在0到255之间 return False 
            return False
        
        return True