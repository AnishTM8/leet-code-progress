# Last updated: 6/22/2025, 7:16:06 PM
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        read = 0
        write = 0

        while read < len(chars):
            char = chars[read]
            count = 0

            while read < len(chars) and char == chars[read]:
                read += 1
                count += 1
            
            chars[write] = char
            write += 1

            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1
        return write 



                    
            
