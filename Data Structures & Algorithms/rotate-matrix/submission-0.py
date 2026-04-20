class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return 

        row, col = len(matrix), len(matrix[0])

        for r in range(row):
            for c in range(r,col):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        for r in range(row):
            matrix[r].reverse()
