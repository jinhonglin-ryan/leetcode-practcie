class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        stack = []
        
        for token in tokens:
            if token in "+-*/":
                num_1 = stack.pop()
                num_2 = stack.pop()
                
                if token == '+':
                    stack.append(num_1 + num_2)
                elif token == '-':
                    stack.append(num_2 - num_1)
                elif token == '*':
                    stack.append(num_2 * num_1)
                elif token == "/":
                    result = int(num_2 / num_1) if num_2 * num_1 > 0 else -(-num_2 // num_1)
                    stack.append(result)
            else:
                stack.append(int(token))
        return stack.pop()
