class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            index = haystack.index(needle)
        except:
            index = -1
        return index


print(Solution().strStr("sadbutsad", "sad"))
print(Solution().strStr("leetcode", "leeto"))
