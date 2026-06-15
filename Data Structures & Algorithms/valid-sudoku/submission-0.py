class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        columns = [set() for i in range(9)]
        squares = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                value = board[i][j]

                if value == ".":
                    continue

                squareIndex = (i // 3) * 3 + (j // 3)
                if value in rows[i] or value in columns[j] or value in squares[squareIndex]:
                    return False
                else:
                    rows[i].add(value)
                    columns[j].add(value)
                    squares[squareIndex].add(value)
        return True
        
