class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = ''
        last_longest_length = 0
        for i in s:
            if (i in substr):
                substr = substr.split(i)[1] + i
            else:
                substr = substr + i
            last_longest_length = max(last_longest_length, len(substr))
        return last_longest_length


solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))
