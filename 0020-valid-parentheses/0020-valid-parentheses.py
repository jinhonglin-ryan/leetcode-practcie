class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if len(s) % 2 != 0:
            return False
        
        stack = list()
        
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            elif c == ")":
                if len(stack) != 0 and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif c == "]":
                if len(stack) != 0 and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            elif c == "}":
                if len(stack) != 0 and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
        
        if len(stack) != 0:
            return False
        
        return True