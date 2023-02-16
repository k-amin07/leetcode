class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows == 1):
            return s
        rows = [''] * numRows
        i = 0
        direction = -1
        for index, letter in enumerate(s):
            if(not index):
                rows[0] = rows[0] + letter
                continue
            if(i == 0 or i == numRows - 1):
                direction = direction * -1

            if(direction == -1):
                i = i - 1
            else:
                i = i + 1

            rows[i] = rows[i] + letter

        return ''.join(rows)


s = Solution()
s.convert("AB", 1)
