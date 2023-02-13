class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if (not (high % 2 and low % 2)):
            count = high - low
        else:
            count = high - low + 1
        if (count % 2):
            return 1 + count // 2
        return count // 2