class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        seen_characters = ''
        max_len = 0
        while(j < len(s)):
            if(s[j] not in seen_characters):
                seen_characters = seen_characters + s[j]
            else:
                max_len = max(j-i, max_len)
                seen_characters = seen_characters.split(s[j])[-1] + s[j]
                i = j - len(seen_characters) + 1
            j = j+1

        return max(j-i, max_len)


solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))
