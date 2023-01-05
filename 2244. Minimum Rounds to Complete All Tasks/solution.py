# initial solution, I was thinking along the lines of coin change problem, 
# which is really unnecessary in this case as we would only have two types 
# of coins (2 and 3).

class Solution_old:
    def minChange(self, change):
        coins = [2,3]
        minCoins = [0] * (change + 1)
        for cents in range(1,change+1):
            minCoins[cents] = float("inf")
            for j in [0,1]:
                if(cents - coins[j] >= 0):
                    result = minCoins[cents-coins[j]]
                    if(result != float("inf")):
                        minCoins[cents] = min(minCoins[cents],result + 1)
        return minCoins[change]



    def minimumRounds(self, tasks: list[int]) -> int:
        count_dict = dict.fromkeys(tasks,0)
        rounds = 0
        for i in tasks:
            count_dict[i] = count_dict[i]+1
        for task, count in count_dict.items():
            curr = self.minChange(count)
            if(curr == float("inf")):
                return -1
            rounds = rounds + curr
        return rounds

# Much simpler solution, if the frequency is divisible by 3, thats the number of rounds needed for that frequency
# if it is not, then we need 1 more round. eg if frequency is 10, then we need 4 rounds,
# two of size 3 and two of size 2. Division by 3 yields 3 and we add 1 to get the required rounds.

from collections import Counter
class Solution:
    def minimumRounds(self, tasks: list[int]) -> int:
        c = Counter(tasks)
        rounds = 0
        for i in c.values():
            if(i == 1):
                return -1
            if(i%3 == 0):
                rounds = rounds + i//3
            else:
                rounds = rounds + i//3 + 1
        return rounds





solution = Solution()
print(solution.minimumRounds([2, 3, 3]))
print(solution.minimumRounds([2,2,3,3,2,4,4,4,4,4]))
print(solution.minimumRounds([66,66,63,61,63,63,64,66,66,65,66,65,61,67,68,66,62,67,61,64,66,60,69,66,65,68,63,60,67,62,68,60,66,64,60,60,60,62,66,64,63,65,60,69,63,68,68,69,68,61]))
print(solution.minimumRounds([69,65,62,64,70,68,69,67,60,65,69,62,65,65,61,66,68,61,65,63,60,66,68,66,67,65,63,65,70,69,70,62,68,70,60,68,65,61,64,65,63,62,62,62,67,62,62,61,66,69]))
print(solution.minimumRounds([119,115,115,119,118,113,118,120,110,113,119,115,116,118,120,117,116,111,113,119,115,113,115,111,112,119,111,111,110,112,113,120,110,111,112,111,119,112,113,112,115,116,113,114,118,119,115,114,114,112,110,117,120,110,117,116,120,118,110,120,119,113,119,120,113,110,120,114,119,115,119,117,120,116,113,113,110,118,117,116,114,114,111,116,119,112,113,116,112,116,119,112,114,114,112,118,116,113,117,116]))
print(solution.minimumRounds([218,211,220,218,211,218,218,217,213,215,219,214,210,210,212,219,214,211,216,218,211,216,218,218,212,210,211,211,215,216,212,219,219,210,217,218,217,217,213,216,217,212,217,219,215,217,215,218,210,218,218,210,212,219,217,214,216,218,220,217,215,215,213,210,212,211,215,218,214,212,211,216,210,216,218,220,211,211,212,218,218,210,215,210,215,213,212,220,217,219,214,216,217,214,215,213,218,219,220,219,215,216,219,218,211,215,210,214,210,215,219,214,212,217,219,215,214,217,213,219,213,218,217,214,216,219,217,217,211,214,214,220,220,216,218,216,220,211,213,219,218,219,215,216,216,220,211,214,212,219,210,215,218,218,220,210,214,211,217,214,220,214,213,210,219,213,214,210,212,216,210,217,211,215,217,213,214,210,217,212,217,216,217,210,211,213,214,220,211,216,214,211,217,211,211,215,219,219,213,216]))