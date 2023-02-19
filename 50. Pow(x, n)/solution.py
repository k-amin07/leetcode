# A more effiecient solution, based on the recurrence relation
# x^n = x * (x^2)^((n-1)/2) if n is odd else (x^2)^(n/2)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(base, exponent):
            if(exponent == 0):
                return 1
            elif(exponent % 2):
                return base * helper(base*base, (exponent-1)//2)
            else:
                return helper(base*base, exponent//2)
        if(n < 0):
            return helper(1/x, n*-1)
        else:
            return helper(x, n)


sol = Solution()
print(sol.myPow(8.84372, -5))

# credits: https://leetcode.com/problems/powx-n/solutions/749109/python-recursive-solution-faster-than-99/?languageTags=python
