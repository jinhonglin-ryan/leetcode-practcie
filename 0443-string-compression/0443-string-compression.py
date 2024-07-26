class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        write_index = 0  # Index to write the next character or number
        read_index = 0  # Index to read the next character

        while read_index < len(chars):
            char = chars[read_index]
            count = 0

            # Count the occurrences of the current character
            while read_index < len(chars) and chars[read_index] == char:
                read_index += 1
                count += 1

            # Write the character to the write_index
            chars[write_index] = char
            write_index += 1

            # If the count is greater than 1, write the count as characters
            if count > 1:
                for digit in str(count):
                    chars[write_index] = digit
                    write_index += 1

        # Return the new length of the array
        return write_index
