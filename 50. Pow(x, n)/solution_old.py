class Solution:
    def myPow(self, x: float, n: int) -> float:
        if(x == 1):
            return x
        if(x == -1 and n % 2):
            return -1
        if(x == -1 and n % 2 == 0):
            return 1
        if(n == -1):
            return 1/x
        if(n == 1):
            return x
        if(n < 0):
            n = n*-1
            x = 1/x
        sol = x
        p = 1
        for i in range(n-1):
            if(p > n):
                break
            sol = sol * sol
            if(p == 1):
                p = 2
            else:
                p = p*2
            if(abs(sol) < 0.0000009 and p < n):
                return 0.00000
        while(p > n):
            p = p - 1
            sol = sol / x

        return sol


sol = Solution()
print(sol.myPow(8.84372, -5))
