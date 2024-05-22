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
                    # 使用 // 运算符实现向零截断
                    result = int(num_2 / num_1) if num_2 * num_1 >= 0 else -(-num_2 // num_1)

                stack.append(result)
            else:
                # 操作数压入栈中
                stack.append(int(token))

        return stack.pop()
