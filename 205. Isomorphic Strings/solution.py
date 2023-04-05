class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s))==len(set(zip(s,t)))==len(set(t))

solution = Solution()
solution.isIsomorphic("egg", "add")
solution.isIsomorphic("foo", "bar")

solution.isIsomorphic("aaaabbbbba", "bbbbaaaaba")

# zip(s,t):  [('a', 'b'), ('a', 'b'), ('a', 'b'), ('a', 'b'), ('b', 'a'), ('b', 'a'), ('b', 'a'), ('b', 'a'), ('b', 'b'), ('a', 'a')]
# set(zip(s,t)): {('a', 'b'), ('b', 'b'), ('a', 'a'), ('b', 'a')}
# here we can see that both a and b map to b
# for strings to be isomorphic, their unique characters must have a 1-1 mapping, which is not the case here
