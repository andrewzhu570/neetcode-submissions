class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeros = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeros.append((i, j))
        
        for row, col in zeros:
            for i in range(len(matrix)):
                matrix[i][col] = 0
            
            for i in range(len(matrix[0])):
                matrix[row][i] = 0
        



        