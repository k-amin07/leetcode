from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        counterRow = [[0 for _ in range(9)] for i in range(9)]
        counterCol = [[0 for _ in range(9)] for i in range(9)]
        counterBlock = [[0 for _ in range(9)] for i in range(9)]
        for indexRow,row in enumerate(board):
            for indexColumn,column in enumerate(row):
                if(column != '.'):
                    counterRow[indexRow][int(column)-1] += 1
                    counterCol[indexColumn][int(column)-1] += 1
                    counterBlock[indexRow//3 * 3 + indexColumn//3][int(column)-1] += 1
        if(max([max(_) for _ in counterRow]) > 1 or max([max(_) for _ in counterCol]) > 1 or  max([max(_) for _ in counterBlock]) > 1):
            return False
        return True
                    

               
    
solution = Solution()
solution.isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])
