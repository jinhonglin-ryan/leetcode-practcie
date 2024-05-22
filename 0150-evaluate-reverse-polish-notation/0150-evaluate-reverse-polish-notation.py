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
                    result = num_2 + num_1
                elif token == '-':
                    result = num_2 - num_1
                elif token == '*':
                    result = num_2 * num_1
                elif token == '/':
                    # 整数除法要向零截断
                    if num_2 * num_1 >= 0:
                        result = int(num_2 / num_1)
                    else:
                        result = -(-num_2 / num_1)

                stack.append(result)
            else:
                
                stack.append(int(token))

        return stack.pop()
