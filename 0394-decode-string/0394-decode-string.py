class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
    
        stack = []
        
        for ch in s:
            if ch != ']':
                stack.append(ch)
            else:
                # 处理括号内的字符串
                tmp = []
                while stack and stack[-1] != '[':
                    tmp.append(stack.pop())
                tmp.reverse()
                
                # 弹出 '['
                stack.pop()
                
                # 处理数字，可能是多位数
                num = []
                while stack and stack[-1].isdigit():
                    num.append(stack.pop())
                num.reverse()
                repeat_count = int("".join(num))
                
                # 将解码后的字符串重复并压入栈中
                stack.extend(tmp * repeat_count)
        
        return "".join(stack)