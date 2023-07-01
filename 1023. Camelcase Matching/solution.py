from typing import List
import re
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        reg = re.compile(r''.join(['[a-z]*' + i for r in pattern for i in r]) + r'[a-z]*')
        res = []
        for i in queries:
            match = reg.match(i)
            if(match):
                res.append(match.group()==i)
            else:
                res.append(False)
        return res