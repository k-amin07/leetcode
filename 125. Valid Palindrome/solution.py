class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum,s)).replace(' ','').lower()
        return s == s[::-1]
    

sol = Solution()
print(
    sol.isPalindrome("A man, a plan, a canal: Panama"),
    sol.isPalindrome("race a car"),
    sol.isPalindrome(" "),
)