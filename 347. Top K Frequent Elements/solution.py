from collections import Counter
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)
        # return list(map(lambda x: x[0],freqs.most_common(k)))
        return [i[0] for i in freqs.most_common(k)]
