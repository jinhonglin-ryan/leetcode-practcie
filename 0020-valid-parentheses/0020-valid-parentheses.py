class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if len(s) % 2 != 0:
            return False
        
        queue = deque()
        
        for c in s:
            if c == "(" or c == "{" or c == "[":
                queue.append(c)
            elif c == ")":
                if len(queue) != 0 and queue[-1] == "(":
                    queue.pop()
                else:
                    return False
            elif c == "]":
                if len(queue) != 0 and queue[-1] == "[":
                    queue.pop()
                else:
                    return False
            elif c == "}":
                if len(queue) != 0 and queue[-1] == "{":
                    queue.pop()
                else:
                    return False
        
        if len(queue) != 0:
            return False
        
        return True