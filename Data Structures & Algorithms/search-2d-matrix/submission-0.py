class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0])
        index = 0
        for i in range(len(matrix)):
            first = matrix[i][0]
            last = matrix[i][n-1]
            if first == target or last == target:
                return True
            if first < target and last > target:
                index = i
        row = matrix[index]
        left = 0
        right = len(row) - 1
        while left <= right:
            mid = (left + right) // 2

            if row[mid] == target:
                return True

            if row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False


    