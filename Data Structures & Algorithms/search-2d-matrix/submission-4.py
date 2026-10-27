class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom :
            row = (top + bottom) // 2
            row_first, row_last = matrix[row][0], matrix[row][-1]

            if target < row_first:
                bottom = row - 1
            elif target > row_last:
                top = row + 1
            else:
                l, r = 0, len(matrix[row]) - 1
                while l <= r:
                    m = (l + r) // 2

                    if target > matrix[row][m]:
                        l = m + 1
                    elif target < matrix[row][m]:
                        r = m - 1
                    else:
                        return True
                return False
        return False