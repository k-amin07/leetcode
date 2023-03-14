class Solution:
    def romanToInt(self, s: str) -> int:
        lookup_table = {'I': 1, 'V': 5, 'X': 10,
                        'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        integer = 0
        for index, num in enumerate(s):
            if (index + 1 == len(s)):
                integer = integer + lookup_table[num]
            elif (num == 'I' and (s[index+1] == 'V' or s[index+1] == 'X')):
                integer = integer - 1
            elif (num == 'X' and (s[index+1] == 'L' or s[index+1] == 'C')):
                integer = integer - 10
            elif (num == 'C' and (s[index+1] == 'D' or s[index+1] == 'M')):
                integer = integer - 100
            else:
                integer = integer + lookup_table[num]
        return integer


solution = Solution()

print(solution.romanToInt("MCMXCIV"))