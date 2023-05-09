from typing import List
from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if(sorted_word in res):
                res[sorted_word].append(word)
            else:
                res[sorted_word] = [word]
        return res.values()

solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
