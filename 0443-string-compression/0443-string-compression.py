class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        w = 0  # Index to write the next character or number
        r = 0  # Index to read the next character

        while r < len(chars):
            char = chars[r]
            cnt = 0

            # Count the occurrences of the current character
            while r < len(chars) and chars[r] == char:
                r += 1
                cnt += 1

            # Write the character to the write_index
            chars[w] = char
            w += 1

            # If the count is greater than 1, write the count as characters
            if cnt > 1:
                for digit in str(cnt):
                    chars[w] = digit
                    w += 1

        # Return the new length of the array
        return w
