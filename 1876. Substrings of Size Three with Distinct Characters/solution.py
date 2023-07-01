class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        l,r = 0,0
        curr = ''
        count = 0
        while(r < len(s)):
            if(s[r] not in curr):
                curr += s[r]
            else:
                curr = curr.split(s[r])[1]
                curr += s[r]
            
            if(len(curr) >= 3):
                curr = curr[1:]
                count += 1
            
            r += 1
        return count

