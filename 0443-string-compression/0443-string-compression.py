class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        w = 0  # 写入的index
        r = 0  # 读取的index

        while r < len(chars):
            char = chars[r]
            cnt = 0

            # 读取连续字符，记录有多少个
            while r < len(chars) and chars[r] == char:
                r += 1
                cnt += 1

            # 写入当前字符
            chars[w] = char
            w += 1

            # 如果当前字符cnt > 1，也需要写入
            if cnt > 1:
                for digit in str(cnt):
                    chars[w] = digit
                    w += 1

        # w是下一个写入的index，即我们目前已经写了多少个（从0开始计算），即最后数组长度
        return w
